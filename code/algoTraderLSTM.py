import streamlit as st
import math
import pandas_datareader.data as web
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM

plt.style.use('fivethirtyeight')

def AlgoPredictPriceLSTM(ticker):
    yf.pdr_override()

    # get stock  quote
    start_date = "2010-01-01"
    end_date = "2020-06-14"
    ticker = "CAT"
    df = web.DataReader(ticker, start=start_date, end=end_date)

    st.write(f"The dataset we will be working with with the stock ticker: {ticker}")
    df

    # visualize the closing price history of the stock at hand:
    fig = plt.figure(figsize=(17, 8))
    plt.title(f"Close Price History of {ticker}")
    plt.xlabel("Date", fontsize=18)
    plt.ylabel("Close Price USD ($)", fontsize=18)
    plt.plot(df['Adj Close'], linewidth=1)
    # plt.show()
    st.pyplot(fig)

    st.write("the dataset downloaded is:")
    st.write(df)
    
    # create new dataframe with only the close price column:
    data = df.filter(['Close'])

    # Convert dataframe to numpy array because of the requirements of the ML NN model:
    stock_dataset = data.values

    # Get the number of rows to train the model and to test it. We'll use 80%
    training_data_len = math.ceil(len(stock_dataset) * .8)

    # scale data. range of scaled data should be between 0 and 1 inclusive:
    scaler = MinMaxScaler(feature_range = (0, 1))
    scaled_dataset = scaler.fit_transform(stock_dataset)


    # Create the scaled training dataset:
    train_data = scaled_dataset[0:training_data_len, :]
    # Split the data into X_train and y_train
    # split the dataset into X_train_scaled, X_test_scaled, y_train, y_test
    X_train = []                  # independent training variable or training features
    y_train = []                  # target variable or dependent variable

    # since we are going to train the model with the past 60 days to predict the closing price 
    # and we are dealing with one stock, which is a single time series of stock prices
    # we get the first 60 days into X_train and the next 60 days into the y_train datasets.
    for i in range(60, len(train_data)):
        X_train.append(train_data[i-60:i, 0])          # from 0 to 59 rows
        y_train.append(train_data[i, 0])               # from 60 row to end of data.

    # display(print(f"X_train data: {len(X_train)}"))
    # display(print(f"y_train data: {len(y_train)}"))
    # display(print(f"X_train: {X_train[0]}"))

    # Convert X_train and y_train to numpy array
    X_train, y_train = np.array(X_train), np.array(y_train)

    # Reshape the shape of the array, because a this moment we have 2-dim arrays and LSTM needs 3-dim arrays.
    X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))
    # X_train[0:2]

    st.write(f"+ Creating a ML model to try to predict the price of [{ticker}] for the very short term....")

    # Build the LSTM neural network model:
    model = Sequential()

    # the model is going to have 2 hidden layers, 
    model.add(LSTM(50, return_sequences=True, input_shape=(X_train.shape[1], 1)))        # input layer
    model.add(LSTM(50, return_sequences=False))
    model.add(Dense(20))
    model.add(Dense(1))


    # Now that we have the model, lets compile it:
    model.compile(optimizer='adam', loss='mean_squared_error')

    # Train the model:
    model.fit(X_train, y_train, batch_size=1, epochs=1)

    # Create a new array containing scaled values from index 1543 to 2003:
    test_data = scaled_dataset[training_data_len - 60: , : ]

    # Create the data set X_test and y_test:
    X_test = []
    y_test = stock_dataset[training_data_len:, :]     # y are the values we want our model to predict. The test values
                                                # the values that the model predict should be similar to the values in y_test.
                                                # this are not scaled values, but rather the original close values downloaded.

    for i in range(60, len(test_data)):
        X_test.append(test_data[i-60:i, 0])

    # Convert dataframe to numpy array because of the requirements of the ML NN model:
    # stock_dataset = stock_data.values
    # Get the number of rows to train the model and to test it. We'll use 80%
    # training_data_len = math.ceil(len(stock_dataset) * .8)
    # make data into numpy array:
    X_test = np.array(X_test)
    # X_test.shape

    # convert the 2-d array to 3-d vector:
    X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
    # X_test.shape

    # Get the models predicted price values:
    predictions = model.predict(X_test)
    # Now convert the predictions back to original scale of values, to compare them with the y_test dataset
    predictions = scaler.inverse_transform(predictions)

    # Visualize the performance of the value to determine the efficiency of the model. 
    # Get the mean square error (RMSE). This is a good measure of how accurate the model can predict the values:
    # It is the std dev. of the residuals. The lower value is a better fit.
    # you should evaluate other measures to really evaluate the performance.

    # a value of 0 is exact prediction, the larger the value of rmse, the poorer the model is.
    # the LOWER the value the better the predictions:

    rmse = np.sqrt(np.mean(predictions-y_test)**2)
    # print(rmse)
    st.write(f"the RMSE for the model is: {rmse}")


    # now we will plot the variables:
    train = data[:training_data_len]
    valid = data[training_data_len:]

    valid.loc[:,'Predictions'] = predictions

    # now we will plot the variables:
    train = data[:training_data_len]
    valid = data[training_data_len:]

    valid.loc[:,'Predictions'] = predictions

    # visualize the data:
    fig = plt.figure(figsize = (16, 8))
    plt.title("Close Price, USD ($)")
    plt.xlabel('Model')
    plt.ylabel("Close Price USD ($)", fontsize=18)
    plt.plot(train['Close'], linewidth=1.5)
    plt.plot(valid['Close'], linewidth=1.5)
    plt.plot(valid['Predictions'], linewidth=2.5)
    plt.legend(['Train', 'Val', 'Predictions'], loc = 'lower right')
    # plt.show()
    st.pyplot(fig)

    st.write("the prediction dataset is:")
    valid

    # get stock  quote
    # start_date = "2010-01-01"
    # end_date = "2020-06-12"


    # Try to predict closing price of ticker stock for :
    ticker_quote = web.DataReader(ticker, start_date, end_date)

    # create a new data frame
    new_df = ticker_quote.filter(['Close'])
    # get the last 60 days closing price values and convert the dataframe to an array
    last_60_days = new_df[-60:].values
    #Scale the data to be values between 0 and 1 to run through model:
    last_60_days_scaled = scaler.transform(last_60_days)

    # Create an empty list:
    X_test = []
    # Append the past 60 days
    X_test.append(last_60_days_scaled)
    #convert the X_test data set to a numpy array and reshape to 3-D
    X_test = np.array(X_test)
    # reshape the data:
    X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
    # Get the predicted values:
    pred_price = model.predict(X_test)

    # undo the scaling: 
    pred_price = scaler.inverse_transform(pred_price)

    # print(pred_price)
    st.write(f"the predicted price by the model is:{pred_price}")

    start_date_test = "2020-06-11"
    end_date_test = "2020-06-16"

    # Try to predict closing price of AAPL stock for :
    ticker_quote2 = web.DataReader(ticker, start_date_test, end_date_test)
    # print(ticker_quote2)
    st.write(ticker_quote2)

    # Try to predict closing price of AAPL stock for :
    ticker_quote2 = web.DataReader(ticker, "2020-06-12", "2020-06-13")
    # print(ticker_quote2)
    st.write(ticker_quote2)
    
    






