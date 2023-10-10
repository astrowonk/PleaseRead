A very minimalistic class to help create emails with tables from dataframes and figures from Plotly. 

This is very much a work in development, see the open Issues for known needed improvements.

Because many email clients (specifically Outlook) don't properly render CSS from the `<style>` tag in the HTML header, this class uses `BeautifulSoup` and `cssutils` to add CSS to each element directly in-line. 

It also is currently hard coded to manually stripe HTML tables like Jupyter's default CSS.

Clone and then it should install with `pip install .`

Usage:

```python
from PleaseRead import Message
m = Message()

m.add_text("## Hello This is an Email")
m.add_readable_time()
m.add_text("You said the meeting could have been an email, so now it is.")
m.add_dataframe(table_df) #pandas dataframe
m.add_figure(fig,img_type='svg') # fig is a plotly figure
m.add_figure(file_path='test.png',caption="Hurricane")
m.preview() ## works in jupyter notebooks 
```

To just get the HTML string use the `m.render_body()` method and pass that as your email body to whatever python mail sending code you prefer. (Sendgrid,postmarker, etc.) I have tested with two Postmarker Python libraries so far.

The above code would produce an email not unlike:

![test](https://github.com/astrowonk/PleaseRead/assets/13702392/ad3beb16-1152-4ee6-b037-5d43b9a660f7)
