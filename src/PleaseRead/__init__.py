from markdown import markdown
from IPython.core.display import display, HTML
import datetime
from PleaseRead.styles import make_header, get_styles
from PleaseRead.utils import (wrap_figure, figure_markdown)
from plotly.graph_objects import Figure
from io import BytesIO
from pandas import DataFrame
from pandas.io.formats.style import Styler
from PleaseRead.InlineStyles import InlineStyles


class Message():
    css_file = None
    body_list = None

    def __init__(self,
                 subject: str | None = None,
                 css_file: str | None = None) -> None:
        """_summary_

        Parameters
        ----------
        subject : str | None, optional
            The emails subject, stored here for convenience, by default None
        header : str | None, optional
            The <header> of the email, setting styles, by default None which loads styles.DEFAULT_HEADER
        """
        if not subject:
            subject = ''  #Stored for convenience only
        self.css_file = css_file
        self.header = make_header()
        self.body_list = []

    def add_text(self, text: str) -> None:
        """Add markdown text to the email.

        Args:
            text (str): Text to add the email, processed with markdown.
        """
        self.body_list.append(text)

    def add_figure(self,
                   fig: Figure | bytes | BytesIO | None = None,
                   img_type: str = 'png',
                   file_path: str | None = None,
                   caption: str | None = None):
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
            wrap_figure(figure_markdown(fig,
                                        img_type=img_type,
                                        file_path=file_path),
                        caption=caption))

    def add_dataframe(self, df: DataFrame | Styler):
        """Add a dataframe as a table to the email.

        Parameters
        ----------
        df : DataFrame | Styler
            The pandas dataframe to be added as a table; could also be a Styler instance.

        """
        self.body_list.append(df.to_html())

    def add_readable_time(self) -> str:
        """Add a date string.

        Returns
        -------
        str
            A nicely formatted date.
        """
        return self.body_list.append(
            datetime.datetime.now().strftime("%a %b %-d, %Y"))

    def render_body(
        self,
        join_string: str = "\n\n",
        apply_inline=True,
    ) -> str:
        """Render the email.

        Parameters
        ----------
        join_string : str, optional
            How to join each object in the email list of elements, by default two returns, "\n\n"

        Returns
        -------
        str
            The email as a string in HTML.
        """
        document = "<!doctype html><html> \n" + self.header + "<body> \n " + markdown(
            join_string.join(self.body_list), extensions=['md_in_html'
                                                          ]) + "</body></html>"

        if apply_inline:
            styler = InlineStyles(css_string=get_styles(self.css_file))
            return styler.apply_rules_to_html(document)
        return document

    def preview(self) -> None:
        """Display the email in Jupyter with display()
        """
        display(HTML(self.render_body()))

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
