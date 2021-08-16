from pstats import Stats

from draw_graph import Graphic
from getdata import GetData
from request import Request
import pandas as pd
import cProfile

from techModel.two_g import twoG

def main():
    raw_data = GetData()
    raw_data.conn_driver()
    raw_data.db_conn()

    request = Request(pd.DataFrame(raw_data.get_data_from_db()))

    two_g = twoG(request.make_request())
    two_g.process_data()
if __name__ == '__main__':



    profiler = cProfile.Profile()
    profiler.runcall(main)  # put main function to check
    stats = Stats(profiler)
    stats.strip_dirs()
    stats.sort_stats("cumulative")
    stats.print_stats()

    #graph = Graphic(raw_data.get_data_from_db(), request.make_request())
    #graph.draw()