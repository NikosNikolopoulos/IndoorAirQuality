# Created on: --
# Data from: 26 May 2017
# @author: --

import pandas as pd
import matplotlib.pyplot as plt


def dateparse(time_from_CSV):
    return pd.to_datetime(time_from_CSV, format='%d/%m/%Y %H:%M:%S')


def populateAxes(ax, data, plot_title):
    ax.plot(data[plot_title])
    ax.text(0.5, 0.9, plot_title, horizontalalignment='center', transform=ax.transAxes)
    return


def plotData(data, _features_to_plot):
    [rows, cols] = _features_to_plot.shape
    rows += 1
    _fig, ax_lst = plt.subplots(nrows=rows, ncols=cols)
    ax_lst.shape = (rows, cols)
    plt.tight_layout()
    plt.subplots_adjust(hspace=0.5)

    _features_to_axes = pd.DataFrame()
    for c in range(cols):
        for r in range(rows-1):
            axSubplt = ax_lst[r, c]
            plot_title = _features_to_plot.loc[r, c]
            _features_to_axes = _features_to_axes.append(pd.DataFrame([[plot_title, axSubplt]]))
            populateAxes(axSubplt, data, plot_title)
            axSubplt.grid(True)
    return _fig, ax_lst


if __name__ == "__main__":
    in_file = 'iaq_hour_dummy_dataset.csv'
    features_to_plot = pd.DataFrame([['temperature'], ['humidity'], ['pm2.5']])
    IAQdata = pd.read_csv(in_file, parse_dates=True, index_col='create_time', date_parser=dateparse)
    fig, _ = plotData(IAQdata, features_to_plot)
    fig.suptitle('IAQ Data', fontsize=10, fontweight='bold')

    PMdata = IAQdata['pm2.5']
    Good_DF = IAQdata[IAQdata['pm2.5'] <= 15.4]

    Moderate_DF = IAQdata[IAQdata['pm2.5'] <= 40.4]
    Moderate_DF = Moderate_DF[Moderate_DF['pm2.5'] >= 15.5]

    Unhealthy1_DF = IAQdata[IAQdata['pm2.5'] <= 65.4]
    Unhealthy1_DF = Unhealthy1_DF[Unhealthy1_DF['pm2.5'] >= 40.5]

    Unhealthy2_DF = IAQdata[IAQdata['pm2.5'] <= 150.4]
    Unhealthy2_DF = Unhealthy2_DF[Unhealthy2_DF['pm2.5'] >= 65.5]

    VeryUnhealthy_DF = IAQdata[IAQdata['pm2.5'] <= 250.4]
    VeryUnhealthy_DF = VeryUnhealthy_DF[VeryUnhealthy_DF['pm2.5'] >= 150.5]

    Hazardous_DF = IAQdata[IAQdata['pm2.5'] <= 500.4]
    Hazardous_DF = Hazardous_DF[Hazardous_DF['pm2.5'] >= 250.5]

    ax2 = fig.add_subplot(4, 1, 4)
    ax2.set_xticklabels([])
    ax2.set_yticklabels([])

    ax2.scatter(Good_DF.index, Good_DF['pm2.5'], color='blue')
    ax2.scatter(Moderate_DF.index, Moderate_DF['pm2.5'], color='g')
    ax2.scatter(Unhealthy1_DF.index, Unhealthy1_DF['pm2.5'], color='y')
    ax2.scatter(Unhealthy2_DF.index, Unhealthy2_DF['pm2.5'], color='r')
    ax2.scatter(VeryUnhealthy_DF.index, VeryUnhealthy_DF['pm2.5'], color='purple')
    ax2.scatter(Hazardous_DF.index, Hazardous_DF['pm2.5'], color='black')

    if len(Good_DF) > 0:
        ax2.hlines(y=15.4, xmin=PMdata.index[0], xmax=PMdata.index[-1], colors='blue', linestyles='--', label='Good')
    if len(Moderate_DF) > 0:
        ax2.hlines(y=40.4, xmin=PMdata.index[0], xmax=PMdata.index[-1], colors='g', linestyles='--', label='Moderate')
    if len(Unhealthy2_DF) > 0:
        ax2.hlines(y=65.4, xmin=PMdata.index[0], xmax=PMdata.index[-1], colors='y', linestyles='--', label='Unhealthy!')
    if len(VeryUnhealthy_DF) > 0:
        ax2.hlines(y=150.4, xmin=PMdata.index[0], xmax=PMdata.index[-1], colors='r', linestyles='--', label='Unhealthy')
    if len(VeryUnhealthy_DF) > 0:
        ax2.hlines(y=250.4, xmin=PMdata.index[0], xmax=PMdata.index[-1], colors='purple', linestyles='--',
                   label='Very unhealthy')
    if len(Hazardous_DF) > 0:
        ax2.hlines(y=500.4, xmin=PMdata.index[0], xmax=PMdata.index[-1], colors='black', linestyles='--',
                   label='Hazardous')

    ax2.text(0.5, 0.9, 'pm2.5 regions', horizontalalignment='center', transform=ax2.transAxes)
    ax2.grid(True)

    plt.show()
