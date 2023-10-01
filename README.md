A very minimalistic class to help create emails with tables from dataframes and figures from Plotly. 

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
![test](https://github.com/astrowonk/PleaseRead/assets/13702392/6a694360-7666-407f-be0c-9fe4b9a7c59c)
