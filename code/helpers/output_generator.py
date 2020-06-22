"""
output_generator.py

Wordt gebruikt om de gewenste output te maken van de wijk

Programmeertheorie
Universiteit van Amsterdam

Jop Rijksbaron, Robin Spiers & Vincent Kleiman
"""
import pandas as pd

def output(neighbourhood, score):
    
    # create the table
    table = []

    # for every house all the corners, name and id are saved in the table
    for i in neighbourhood:
        corner_1 = str(int(i.x0)) + "," + str(int(i.y0))
        corner_2 = str(int(i.y1)) + "," + str(int(i.y0))
        corner_3 = str(int(i.y1)) + "," + str(int(i.x1))
        corner_4 = str(int(i.x0)) + "," + str(int(i.x1))
        table.append([str(i.name)+"_"+ str(i.id), corner_1, corner_2, corner_3, corner_4, i.name])
    
    # the last row of the table needs to have the networth value
    table.append(["networth", score])

    # turn the table into a dataframe
    df = pd.DataFrame(table, columns=["structure", "corner_1", "corner_2", "corner_3", "corner_4", "type"]).set_index("structure")
    
    # save the dataframe as a csv file
    df.to_csv("output.csv")
    
    # return the dataframe
    return df