from yellowbrick.regressor import ResidualsPlot
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error


def model(model, x_train, y_train, x_test, y_test):
    y_train = y_train.reshape(-1,)
    y_test = y_test.reshape(-1,)
    #Fitting the linear regression model with the training data
    visualizer = ResidualsPlot(model)
    visualizer.fit(x_train, y_train)

    #Returning the r-squared score from the model on the test data
    visualizer.score(x_test,y_test)
    visualizer.show()
    y_pred_train = visualizer.predict(x_train)
    y_pred_test = visualizer.predict(x_test)

    rmse_test = round(mean_squared_error(y_test,
                                         y_pred_test,
                                         squared=False),
                 2)

    rmse_train = round(mean_squared_error(y_train,
                                          y_pred_train,
                                          squared=False),
                       2)

    mae_test = round(mean_absolute_error(y_test,
                                         y_pred_test),
                 2)


    mae_train = round(mean_absolute_error(y_train,
                                     y_pred_train),
             2)



    rmse_test = sc_y.inverse_transform(rmse_test.reshape(-1,1))[0][0]
    rmse_train = sc_y.inverse_transform(rmse_train.reshape(-1,1))[0][0]
    mae_test = sc_y.inverse_transform(mae_test.reshape(-1,1))[0][0]
    mae_train = sc_y.inverse_transform(mae_train.reshape(-1,1))[0][0]

    r2_test = round(r2_score(y_test,
                             y_pred_test),
               4)

    r2_train = round(r2_score(y_train,
                              y_pred_train),
                     4)





    print("The model performance")
    print("---------------------")
    print(f"RMSE of the train is {rmse_train:,}")
    print(f"RMSE of the test set is {rmse_test:,}")
    print(f"MAE of the train is {mae_train:,}")
    print(f"MAE of the test set is {mae_test:,}")
    print(f"R2 score of train set is {r2_train}")
    print(f"R2 score of test set is {r2_test}")
    print(f"Y scaler: {scaler_y}")
    print(f"X scaler: {scaler_x}")


    case = {"Model": model,
        "Inputs":feature_names,
        "X-scale": scaler_x,
        "Y-scale": scaler_y,
        "train-R2": r2_train,
        "test-R2": r2_test,
        "test-MAE":mae_test,
        "train-MAE":mae_train,
        "train-RMSE": format(rmse_train, ','),
        "test-RMSE": format(rmse_test, ',')}

    model_outputs.append(case)

