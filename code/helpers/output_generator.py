import pandas as pd

def output(neighbourhood, score):
    table = []
    for i in neighbourhood:
        corner_1 = str(int(i.x0)) + "," + str(int(i.y0))
        corner_2 = str(int(i.y1)) + "," + str(int(i.y0))
        corner_3 = str(int(i.y1)) + "," + str(int(i.x1))
        corner_4 = str(int(i.x0)) + "," + str(int(i.x1))
        table.append([str(i.name)+"_"+ str(i.id), corner_1, corner_2, corner_3, corner_4, i.name])
    
    table.append(["networth", score])

    # turn the table into a dataframe
    df = pd.DataFrame(table, columns=["structure", "corner_1", "corner_2", "corner_3", "corner_4", "type"]).set_index("structure")

    # save the dataframe as a csv file
    return df