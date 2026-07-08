# 📊 Create Multiple Excel Sheets with Pandas

This project demonstrates how to create multiple **Pandas DataFrames** and save them into a single Excel workbook using different worksheets.

Instead of reading existing data, the data is created directly in Python and exported to an Excel file with separate sheets for **Cost** and **Revenue**.

---

## 📌 What You'll Learn

- Create DataFrames using Python dictionaries
- Store tabular data with Pandas
- Write multiple DataFrames to a single Excel file
- Create separate worksheets using `ExcelWriter`
- Export data to Excel

---

## 📂 Project Structure

```
Project/
│── Pandas.py
│── product_cost_revenue_merged.xlsx
│── README.md
```

---

## 🐍 Python Code

```python
import pandas as pd

df_cost = pd.DataFrame({
    'Category': ['Home Decore', 'Fashion', 'Home'],
    'Unit': [123, 343, 45],
    'Price': [3114, 5676, 6741]
})

df_revenue = pd.DataFrame({
    'Category': ['Home Decore', 'Fashion', 'Home'],
    'Unit': [234, 567, 765],
    'Revenue': [34564, 64544, 74623]
})

print(df_cost)
print(df_revenue)

with pd.ExcelWriter('product_cost_revenue_merged.xlsx') as writer:
    df_cost.to_excel(writer, sheet_name='Cost')
    df_revenue.to_excel(writer, sheet_name='Revenue')
```

---

## 📄 Excel Output

After running the script, an Excel workbook named:

```
product_cost_revenue_merged.xlsx
```

will be created with two worksheets.

### Sheet 1 — Cost

| Category | Unit | Price |
|----------|-----:|------:|
| Home Decore | 123 | 3114 |
| Fashion | 343 | 5676 |
| Home | 45 | 6741 |

### Sheet 2 — Revenue

| Category | Unit | Revenue |
|----------|-----:|--------:|
| Home Decore | 234 | 34564 |
| Fashion | 567 | 64544 |
| Home | 765 | 74623 |

---

## 💻 Requirements

- Python 3.x
- Pandas
- OpenPyXL

Install the required packages:

```bash
pip install pandas openpyxl
```

---

## ▶️ Run the Project

```bash
python Pandas.py
```

---

## 🎯 Why This Project?

When working with Excel files, it's common to organize related data into separate worksheets. This project shows how to automate that process with Pandas, making it easier to generate structured Excel reports directly from Python.

---

### ⭐ If you found this project useful, consider giving it a star on GitHub!
