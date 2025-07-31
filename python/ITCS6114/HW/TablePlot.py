import matplotlib.pyplot as plt

# Sample data for the table
data = [['Row 1, Col 1', 'Row 1, Col 2'],
        ['Row 2, Col 1', 'Row 2, Col 2']]
col_labels = ['Column A', 'Column B']
row_labels = ['Row X', 'Row Y']

fig, ax = plt.subplots()

# Hide axes for a cleaner table-only presentation
ax.axis('off')

# Create the table
table = ax.table(cellText=data,
                 colLabels=col_labels,
                 rowLabels=row_labels,
                 loc='center') # Position of the table

# Optional: Adjust table properties (e.g., font size)
table.auto_set_font_size(False)
table.set_fontsize(10)

plt.show()