"""
output_generator.py

Wordt gebruikt om de gewenste output te maken van de wijk

Programmeertheorie
Universiteit van Amsterdam

Jop Rijksbaron, Robin Spiers & Vincent Kleiman
"""
import pandas as pd
import datetime

def output(neighbourhood, score, algorithm, iterations, max_houses, water_layout, ts):
    """"creates the desired output which contains names, types and coordinates of the corners per object"""
    
    # create the table
    table = []

    # for every house all the corners, name and id are saved in the table
    for i in neighbourhood:
        corner_1 = str(int(i.x0)) + "," + str(int(i.y0))
        corner_2 = str(int(i.x1)) + "," + str(int(i.y0))
        corner_3 = str(int(i.x1)) + "," + str(int(i.y1))
        corner_4 = str(int(i.x0)) + "," + str(int(i.y1))
        table.append([str(i.name)+"_"+str(i.id), corner_1, corner_2, corner_3, corner_4, i.name])
    
    # the last row of the table needs to have the networth value
    table.append(["networth", int(score)])

    # turn the table into a dataframe
    df = pd.DataFrame(table, columns=["structure", "corner_1", "corner_2", "corner_3", "corner_4", "type"]).set_index("structure")
    
    # update output.csv file
    df.to_csv("results/output.csv")

    # archive the dataframe as a csv file
    df.to_csv("results/archive/"+ts+"-output-"+str(algorithm)+"-"+str(iterations)+"-"+str(max_houses)+"-"+str(water_layout)+".csv")
    
    # return the dataframe
    return df