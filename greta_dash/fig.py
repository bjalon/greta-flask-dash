import plotly.express as px

# fig = px.bar(data, x="Fruit", y="Amount", color="City", barmode="group")
df = px.data.tips()
fig = px.box(df, x="time", y="total_bill")