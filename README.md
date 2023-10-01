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
