from markdown import markdown
from plotly.graph_objects import Figure as plotly_figure
import base64
from io import BytesIO
from IPython.core.display import display, HTML
import datetime
from styles import DEFAULT_HEADER


def encode_plotly(fig, img_type='png'):
    return base64.b64encode(
        fig.to_image(width=900, height=750, scale=2,
                     format=img_type)).decode('utf-8')


def encode_bytes_io(my_bytes_io):
    my_bytes_io.seek(0)
    return base64.b64encode(my_bytes_io.read()).decode('utf-8')


def encode_bytes(some_bytes):
    return base64.b64encode(some_bytes).decode('utf-8')


def get_bytes_from_path(file_path):
    with open(file_path, 'rb') as f:
        return f.read()


def figure_markdown(fig=None, file_path=None, alt_text=None, img_type='png'):
    if fig:
        assert isinstance(fig,
                          (plotly_figure, bytes,
                           BytesIO)), "Figure must be image bytes or plotly"
    if not fig:
        assert file_path, "Requires figure or bytes, or a file_path"
        fig = get_bytes_from_path(file_path=file_path)
        print(type(fig))

    mime_type = img_type
    if img_type == 'svg':
        assert (isinstance(
            fig, plotly_figure)), "SVG only supported for plotly figures"
        mime_type = 'svg+xml'

    if isinstance(fig, plotly_figure):
        return f"![{alt_text}](data:image/{mime_type};base64,{encode_plotly(fig,img_type=img_type)})"
    if isinstance(
            fig,
            BytesIO,
    ):
        return f"![{alt_text}](data:image/{mime_type};base64,{encode_bytes_io(fig)})"
    if isinstance(
            fig,
            bytes,
    ):
        return f"![{alt_text}](data:image/{mime_type};base64,{encode_bytes(fig)})"


def wrap_figure(fig_markdown, caption):
    if not caption:
        return fig_markdown
    return f"""<figure markdown="1">\n\n{fig_markdown}\n\n<figcaption align = "center"><b>{caption}</b></figcaption>\n\n</figure>"""


class Message():
    body_list = None

    def __init__(self, subject=None, body_list=None, header=None) -> None:
        if not body_list:
            self.body_list = []
        if not subject:
            self.subject = ''
        if header:
            self.header = header
        else:
            self.header = DEFAULT_HEADER

    def add_text(self, text):
        self.body_list.append(text)

    def add_figure(self,
                   fig=None,
                   img_type='png',
                   file_path=None,
                   caption=None):
        self.body_list.append(
            wrap_figure(figure_markdown(fig,
                                        img_type=img_type,
                                        file_path=file_path),
                        caption=caption))

    def add_dataframe(self, df):
        self.body_list.append(df.to_html())

    def add_readable_time(self):
        return self.body_list.append(
            datetime.datetime.now().strftime("%a %b %-d, %Y"))

    def render_body(self, join_string="\n\n"):
        return self.header + markdown(join_string.join(self.body_list),
                                      extensions=['md_in_html']) + "</html>"

    def preview(self):
        display(HTML(self.render_body()))

    def save_html(self):
        output = self.render_body()
        with open('test.html', 'w') as f:
            f.write(output)
