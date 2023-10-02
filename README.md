A very minimalistic class to help create emails with tables from dataframes and figures from Plotly. 

This is very much a work in development, see the open Issues for known needed improvements.

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
```

That should produce an email not unlike:

![test](https://github.com/astrowonk/PleaseRead/assets/13702392/ad3beb16-1152-4ee6-b037-5d43b9a660f7)
