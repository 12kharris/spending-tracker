
# in future would want this stored in the db with a link to user
# so they can customise the colours of each category

def generate_category_colours():
    transaction_cat_colours = dict()
    transaction_cat_colours["Car"] = "#fc0303"
    transaction_cat_colours["Groceries"] = "#1703fc"
    transaction_cat_colours["Dining Out"] = "#a903fc"
    transaction_cat_colours["Subscriptions"] = "#03c6fc"
    transaction_cat_colours["Clothes"] = "#d3f54c"
    transaction_cat_colours["Leisure"] = "#0c6b01"
    transaction_cat_colours["Housing"] = "#f56b02"
    transaction_cat_colours["Education"] = "#02f502"
    transaction_cat_colours["Presents"] = "#f5f502"
    transaction_cat_colours["Miscellaneous"] = "#f50288"
    transaction_cat_colours["Unassigned"] = "#999798"

    return transaction_cat_colours