import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def train_test_split_graph(Y_train,Y_test):
    fig, ax = plt.subplots(figsize=(15, 6))
    Y_train.plot(ax=ax, label='Training Set', title='Data Train/Test Split')
    Y_test.plot(ax=ax, label='Test Set')
    ax.legend(['Training Set', 'Test Set'])
    plt.show()

    

def scatter_test_pred(Y_test,Y_pred):
    # Visualize the predicted vs. actual values
    plt.scatter(Y_test, Y_pred)
    plt.xlabel("Sirta GHI")
    plt.ylabel("Predictid GHI")
    plt.title("Sirta vs. Predicted GHI")
    plt.show()
    
def scatter_test_pred_density(Y_test, Y_pred):
    # Concatenate the two arrays
    data = pd.DataFrame({'Y_test': Y_test, 'Y_pred': Y_pred})

    # Create a scatter plot
    plt.scatter(Y_test, Y_pred, alpha=0.5)

    # Create a 2D kernel density estimation plot
    sns.kdeplot(data=data, x='Y_test', y='Y_pred', cmap="Blues", fill=True, thresh=0, levels=100, alpha=0.3)

    plt.xlabel("Sirta GHI")
    plt.ylabel("Predicted GHI")
    plt.title("Sirta vs. Predicted GHI with Density Visualization")
    plt.show()
    
def plot_test_pred(Y_test,Y_pred):
    plt.figure(figsize=(12, 6))
    plt.plot(Y_test.index, Y_test, label='Valeurs Réelles', marker='o')
    plt.plot(Y_test.index, Y_pred, label='Valeurs Prédites', linestyle='--', marker='x')
    plt.xlabel('Dates')
    plt.ylabel('Valeurs')
    plt.title('Comparaison des Valeurs Réelles et Prédites')
    plt.legend()
    plt.grid(True)
    plt.show()
    
def zoom_plot_test_pred(Y_test,Y_pred,num_values_to_plot=200):
    plt.figure(figsize=(12, 6))
    plt.plot(Y_test.index[:num_values_to_plot], Y_test.iloc[:num_values_to_plot], label='Valeurs Réelles', marker='o')
    plt.plot(Y_test.index[:num_values_to_plot], pd.DataFrame(Y_pred).iloc[:num_values_to_plot], label='Valeurs Prédites', linestyle='--', marker='x')
    plt.xlabel('Dates')
    plt.ylabel('Valeurs')
    plt.title('Comparaison des Valeurs Réelles et Prédites (Zoom sur les 200 premières valeurs)')
    plt.legend()
    plt.grid(True)
    plt.xlim(Y_test.index[0], Y_test.index[num_values_to_plot-1])
    plt.show()
    
def difference(Y_test,Y_pred):
    difference = Y_test-Y_pred.squeeze()
    plt.figure(figsize=(12, 6))
    plt.plot(Y_test.index, difference, label='Différence (Réelles - Prédites)', marker='o', color='red')
    plt.xlabel('Dates')
    plt.ylabel('Différence')
    plt.title('Différence entre les Valeurs Réelles et Prédites (Toutes les valeurs)')
    plt.legend()
    plt.grid(True)
    plt.show()
    
def zoom_difference(Y_test,Y_pred,num_values_to_plot=200):
    difference = Y_test-Y_pred.squeeze()
    plt.figure(figsize=(12, 6))
    plt.plot(Y_test.index[:num_values_to_plot], difference[:num_values_to_plot], marker='o', color='red')
    plt.xlabel('Dates')
    plt.ylabel('Différence')
    plt.title('Différence entre les Valeurs Réelles et Prédites (Zoom sur les 200 premières valeurs)')
    plt.grid(True)
    plt.show()
    
def all_test_pred_graph(Y_test,Y_pred,num_values_to_plot=200):
    plot_test_pred(Y_test,Y_pred)
    zoom_plot_test_pred(Y_test,Y_pred,num_values_to_plot)
    difference(Y_test,Y_pred)
    zoom_difference(Y_test,Y_pred,num_values_to_plot)
    
def mesures_results(df_sat_ev):
    fig, axes = plt.subplots(nrows=4, ncols=1, figsize=(10, 12))

    axes[0].plot(df_sat_ev.index, df_sat_ev['MSE'], label='MSE', color='blue')
    axes[0].set_ylabel('MSE')
    axes[0].legend()

    axes[1].plot(df_sat_ev.index, df_sat_ev['MAE'], label='MAE', color='green')
    axes[1].set_ylabel('MAE')
    axes[1].legend()

    axes[2].plot(df_sat_ev.index, df_sat_ev['R2'], label='R2', color='red')
    axes[2].set_ylabel('R2')
    axes[2].legend()

    axes[3].plot(df_sat_ev.index, df_sat_ev['DTW'], label='DTW Distance', color='purple')
    axes[3].set_ylabel('DTW Distance')
    axes[3].legend()

    plt.xlabel('Index')
    plt.tight_layout()
    plt.show()

def features_importance(model, X_train):
    feat_importances=pd.Series(model.feature_importances_,index=X_train.columns).sort_values(ascending=True)
    feat_importances.plot(kind ='barh')
    
