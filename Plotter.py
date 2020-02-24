import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import copy

class plotter:

    def __init__(self, data_frame):
        self.data = data_frame
        self.fig = plt.figure()

    def plot_continuous_var_vs_income(self, column,
                                      max_gross = None, min_gross = None,
                                      max_rating = None, min_rating = None,
                                      max_count = None, min_count = None,
                                      oldest = None, newest = None,
                                      acceptable_genres = None):
        #plot GDP vs income
        if not column in self.data.columns:
            return None

        df = copy.copy(self.data)

        #convert strings
        df['World Wide Gross'] = pd.to_numeric(df['World Wide Gross'])
        df['Ratings'] = pd.to_numeric(df['Ratings'])
        df['Number of Ratings'] = pd.to_numeric(df['Number of Ratings'])
        df['Release Date'] = pd.to_datetime(df['Release Date'])

        #Apply Filters
        df = prune_df(df,
                      max_gross, min_gross,
                      max_rating, min_rating,
                      max_count, min_count,
                      oldest, newest,
                      acceptable_genres)

        X = np.array([float(val) for (val, y) in zip(df[column], df['World Wide Gross']) if not pd.isna(y)])
        Y = np.array([float(val) for val in df['World Wide Gross'] if not pd.isna(val)])

        plt.scatter(X, Y)
        plt.xlabel(column)
        plt.ylabel('World Wide Gross')
        plt.title('{} vs World Wide Gross'.format(column))

    def plot_release_date_vs_income(self,
                                    max_gross = None, min_gross = None,
                                    max_rating = None, min_rating = None,
                                    max_count = None, min_count = None,
                                    oldest = None, newest = None,
                                    acceptable_genres = None):

        #Plot time series data vs world wide gross
        df = self.data

        #COnvert strings
        df['World Wide Gross'] = pd.to_numeric(df['World Wide Gross'])
        df['Ratings'] = pd.to_numeric(df['Ratings'])
        df['Number of Ratings'] = pd.to_numeric(df['Number of Ratings'])
        df['Release Date'] = pd.to_datetime(df['Release Date'])

        #Apply filters
        df = prune_df(df,
                      max_gross, min_gross,
                      max_rating, min_rating,
                      max_count, min_count,
                      oldest, newest,
                      acceptable_genres)


        X = np.array([val for (val, y) in zip(df['Release Date'], df['World Wide Gross']) if not pd.isna(y)])
        Y = np.array([float(val) for val in df['World Wide Gross'] if not pd.isna(val)])
        plt.plot_date(X, Y)
        plt.xlabel('Release Date')
        plt.ylabel('World Wide Gross')
        plt.title('Release Date vs World Wide Gross')


    def plot_genre_vs_income(self,
                             max_gross = None, min_gross = None,
                             max_rating = None, min_rating = None,
                             max_count = None, min_count = None,
                             oldest = None, newest = None,
                             acceptable_genres = None):
        #Catagorically plot the average gross of each genre
        df = self.data

        #Convert strigs to usable types
        df['World Wide Gross'] = pd.to_numeric(df['World Wide Gross'])
        df['Ratings'] = pd.to_numeric(df['Ratings'])
        df['Number of Ratings'] = pd.to_numeric(df['Number of Ratings'])
        df['Release Date'] = pd.to_datetime(df['Release Date'])

        #Apply filters
        df = prune_df(df,
                      max_gross, min_gross,
                      max_rating, min_rating,
                      max_count, min_count,
                      oldest, newest,
                      acceptable_genres)

        vals = {}
        for (genres, gross) in zip(df['Genres'], df['World Wide Gross']):
            if not pd.isna(gross):
                genres = genres.split()
                for genre in genres:
                    if genre in vals.keys():
                        vals[genre].append(gross)
                    else:
                        vals[genre] = [gross]

        Y = np.array([category for category in vals.keys()])
        X = np.array([sum(grosses) / len(grosses) for grosses in vals.values()])
        y_pos = np.arange(len(Y))
        plt.bar(y_pos, X, align='center', alpha=0.5)
        plt.xticks(y_pos, Y)
        plt.ylabel('World Wide Gross')
        plt.title('Genera vs Average World Wide Gross')

    def plot_gross_hist(self,
                        max_gross = None, min_gross = None,
                        max_rating = None, min_rating = None,
                        max_count = None, min_count = None,
                        oldest = None, newest = None,
                        acceptable_genres = None):

        df = self.data

        # Convert strigs to usable types
        df['World Wide Gross'] = pd.to_numeric(df['World Wide Gross'])
        df['Ratings'] = pd.to_numeric(df['Ratings'])
        df['Number of Ratings'] = pd.to_numeric(df['Number of Ratings'])
        df['Release Date'] = pd.to_datetime(df['Release Date'])

        # Apply filters
        df = prune_df(df,
                      max_gross, min_gross,
                      max_rating, min_rating,
                      max_count, min_count,
                      oldest, newest,
                      acceptable_genres)

        X = np.array([float(val) for val in df['World Wide Gross'] if not pd.isna(val)])

        plt.hist(X)
        plt.xlabel('World Wide Gross')
        plt.ylabel('Count')
        plt.title('World Wide Gross Distribution')



    def plot(self, column,
             max_gross = None, min_gross = None,
             max_rating = None, min_rating = None,
             max_count = None, min_count = None,
             oldest = None, newest = None,
             acceptable_genres = None):
        if column == 'Genres':
            self.plot_genre_vs_income(max_gross, min_gross,
                                      max_rating, min_rating,
                                      max_count, min_count,
                                      oldest, newest,
                                      acceptable_genres)
        elif column == 'Release Date':
            self.plot_release_date_vs_income(max_gross, min_gross,
                                             max_rating, min_rating,
                                             max_count, min_count,
                                             oldest, newest,
                                             acceptable_genres)
        elif column == 'World Wide Gross':
            self.plot_gross_hist(max_gross, min_gross,
                                 max_rating, min_rating,
                                 max_count, min_count,
                                 oldest, newest,
                                 acceptable_genres)
        elif column in ['Ratings', 'Number of Ratings', 'World Wide Gross']:
            self.plot_continuous_var_vs_income(column,
                                               max_gross, min_gross,
                                               max_rating, min_rating,
                                               max_count, min_count,
                                               oldest, newest,
                                               acceptable_genres)
        plt.show()


def prune_df(data,
             max_gross = None, min_gross = None,
             max_rating = None, min_rating = None,
             max_count = None, min_count = None,
             oldest = None, newest = None,
             acceptable_genres = None):

    #Remove any rows of data not subject to contraints

    pruned_data = data

    if not max_gross is None:
        pruned_data = pruned_data[pruned_data['World Wide Gross'] <= max_gross]

    if not min_gross is None:
        pruned_data = pruned_data[pruned_data['World Wide Gross'] >= min_gross]

    if not max_rating is None:
        pruned_data = pruned_data[pruned_data['Ratings'] <= max_rating]

    if not min_rating is None:
        pruned_data = pruned_data[pruned_data['Ratings'] >= min_rating]

    if not max_count is None:
        pruned_data = pruned_data[pruned_data['Number of Ratings'] <= max_count]

    if not min_count is None:
        pruned_data = pruned_data[pruned_data['Number of Ratings'] >= min_count]

    if not oldest is None:
        i = [(date.year >= oldest) for date in pruned_data['Release Date']]
        pruned_data = pruned_data[i]

    if not newest is None:
        i = [(date.year <= newest) for date in pruned_data['Release Date']]
        pruned_data = pruned_data[i]

    if not acceptable_genres is None:
        i = [any(elem in genre_set.split(' ') for elem in acceptable_genres.split(' ')) for genre_set in pruned_data['Genres']]
        pruned_data = pruned_data[i]

    return pruned_data


