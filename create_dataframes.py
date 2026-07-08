import pandas as pd

df_cost = pd.DataFrame({
    'Category' :['Home Decore', 'Fashion', 'Home', ],
    'Unit' :[123, 343, 45],
    'Price' :[3114,5676,6741]
})
df_revenue = pd.DataFrame({
    'Category' :['Home Decore', 'Fashion', 'Home'],
    'Unit' :[234, 567, 765],
    'Revenue' :[34564, 64544, 74623]
})

print(df_cost)
print(df_revenue)



with pd.ExcelWriter('product_cost_revenue_merged.xlsx') as writer:
    df_cost.to_excel(writer, sheet_name='Cost')
    df_revenue.to_excel(writer, sheet_name='Revenue')

