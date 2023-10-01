from plotly.graph_objects import Figure as plotly_figure
import base64
from io import BytesIO


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
