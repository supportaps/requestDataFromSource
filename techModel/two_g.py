import gc

from matplotlib.figure import Figure

from techModel.technologie import Technologie
import pandas as pd

from matplotlib.backends.backend_pdf import PdfPages
from config import Config

class twoG(Technologie):

    def __init__(self):

        self.config = Config()

    def process_data(self):

        with PdfPages('source_data.pdf') as pdf_pages:
            for item in self.sta:
                result_pd_data = pd.DataFrame(item) # got data site by site
                print("RESULT_PD_DATA: ", result_pd_data)

                unique_cell_list = result_pd_data.IDDD.unique() # get list of unique cell names

                print("RESULT_PD_DATA: ", unique_cell_list)

                for unique_cell in unique_cell_list:
                    d1 = result_pd_data[result_pd_data[self.config.config_kpi()[2]] == unique_cell]

                    fig = Figure(figsize=(8.27, 11.69), dpi=100)
                    fig.suptitle(unique_cell)
                    ax = fig.add_subplot(1, 1, 1)
                    ax.set_ylabel(self.config.config_kpi()[0])
                    ax.plot(self.config.config_kpi()[1], self.config.config_kpi()[0], data=d1, color='red', marker='o', alpha=0.5, linewidth=2.5, markersize=3)
                    ax.fill_between(self.config.config_kpi()[1], self.config.config_kpi()[0], data=d1, facecolor='red', alpha=0.2)







                    pdf_pages.savefig(fig)

                    ax.clear()
                    fig.clear()
                    fig.clf()


                #with open("Check_Data.txt", "a") as file:
                   #file.write(str(d1))
                #plt.show()
        pdf_pages.close()
