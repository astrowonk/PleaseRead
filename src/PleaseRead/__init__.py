import datetime
from io import BytesIO
from pathlib import Path

import css_inline
from altair import Chart
from great_tables import GT
from IPython.display import HTML, display
from markdown import markdown
from pandas import DataFrame
from pandas.io.formats.style import Styler
from plotly.graph_objects import Figure

from PleaseRead.utils import figure_markdown, wrap_figure


class Message:
    """A helper class to create simple HTML email messages from markdown, dataframes, and figures.

    Parameters
    ----------
    subject : str | None, optional
        The email subject stored only for convenience, by default None
    css_file : str | None, optional
        A css file for the message, by default None
    """

    css_file = None
    body_list = None

    def __init__(self, subject: str | None = None, css_file: str | None = None) -> None:
        if not subject:
            subject = ''  # Stored for convenience only
        self.css_file = css_file
        self.body_list = []

    def __add__(self, other):
        new_class = Message()
        new_class.body_list = self.body_list + other.body_list
        return new_class

    @staticmethod
    def make_header(styles: str = None) -> str:
        """Make the header with styles if available.

        Parameters
        ----------
        styles : str, optional
            A block of CSS as a string, by default None

        Returns
        -------
        str
            An html header with our without the included styles.
        """
        if not styles:
            styles = ''
        return f"""<head><title></title> {styles}</head>"""

    def add_text(self, text: str) -> None:
        """Add markdown text to the email.

        Args:
            text (str): Text to add the email, processed with markdown.
        """
        self.body_list.append(text)

    def add_figure(
        self,
        fig: Figure | bytes | BytesIO | Chart | None = None,
        img_type: str = 'png',
        file_path: str | None = None,
        caption: str | None = None,
        width=None,
        height=None,
    ):
        """Add a figure to the image, can be bytes or a Plotly figure object.

        Parameters
        ----------
        fig : Figure | bytes | BytesIO | None, optional
             A Plotly Figure or BytesIO/bytes of an image, by default None
        img_type : str, optional
            The image type. Could be xml, jpg, etc., by default 'png'
        file_path : str | None, optional
            The string pointing to a file path for an image, by default None
        caption : str | None, optional
            A caption added as a figcaption to the image. by default None
        """

        self.body_list.append(
            wrap_figure(
                figure_markdown(
                    fig,
                    img_type=img_type,
                    file_path=file_path,
                    width=width,
                    height=height,
                ),
                caption=caption,
            )
        )

    def add_dataframe(self, item: DataFrame | Styler | GT):
        """Add a dataframe as a table to the email.

        Parameters
        ----------
        df : DataFrame | Styler
            The pandas dataframe to be added as a table; could also be a Styler instance.

        """
        if isinstance(item, GT):
            self.body_list.append(item.as_raw_html(inline_css=True))
        else:
            self.body_list.append(item.to_html())

    def add_readable_time(self) -> str:
        """Add a date string.

        Returns
        -------
        str
            A nicely formatted date.
        """
        return self.body_list.append(datetime.datetime.now().strftime('%a %b %-d, %Y'))

    def render_body(
        self,
        join_string: str = '\n\n',
        apply_inline=True,
        minimal_render=False,
    ) -> str:
        """Return Message rendered as HTML.

        Parameters
        ----------
        join_string : str, optional
            With what strring to join each inserted element together.
        apply_inline : bool, optional
            Turn CSS into inline styles, by default True. If False, style information will be placed in HTML header (and
            mostly not work in Outlook)

        Returns
        -------
        str
            The Message as an HTML string.
        """

        if minimal_render:
            document = markdown(join_string.join(self.body_list), extensions=['md_in_html'])
        else:
            ext_list = ['md_in_html', 'toc']
            document = (
                '<!doctype html><html> \n'
                + self.make_header()
                + '<body> \n '
                + markdown(join_string.join(self.body_list), extensions=ext_list)
                + '</body></html>'
            )

        if apply_inline:
            # styles/email is relative to the current directory
            script_dir = Path(__file__).parent
            with open(f'{script_dir}/default.css') as f:
                css = f.read()
            inliner = css_inline.CSSInliner(extra_css=css)
            print(inliner)
            return inliner.inline(document)

        return document

    def preview(self, **kwargs) -> None:
        """Display the email in Jupyter with display()"""
        display(HTML(self.render_body(**kwargs)))

    def save_html(self, file_name: str) -> None:
        """Save the output to a file for testing/inspection.

        Parameters
        ----------
        file_name : str
            The file name of the saved html file.
        """
        output = self.render_body()
        with open(file_name, 'w') as f:
            f.write(output)
