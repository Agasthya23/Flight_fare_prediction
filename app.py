from flask import Flask, redirect,url_for,request, render_template
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open("Flightfare_predictor.pkl", "rb"))



@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict/<float:price>")
def predict(price):
    return render_template('home.html',result=price)




@app.route("/submit", methods = ["GET", "POST"])
def submit():
    if request.method == "POST":

        Additional_Info=int(request.form['Additional_Info'])

        # Date_of_Journey
        date_dep = request.form["Dep_Time"]
        Date = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").day)
        Month = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").month)
        

        # Departure
        Dep_Hour = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").hour)
        Dep_Min = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").minute)
        

        # Arrival
        date_arr = request.form["Arrival_Time"]
        Arrival_Hour = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").hour)
        Arrival_Minute = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").minute)
        

        # Duration
        Duration_H = abs(Arrival_Hour - Dep_Hour)
        Duration_M = abs(Arrival_Minute - Dep_Min)
        

        # Total Stops
        Total_Stops = int(request.form["stops"])
        # print(Total_stops)

        # Airline
        # AIR ASIA = 0
        airline=request.form['airline']
        if(airline=='Jet Airways'):
            Airline_Jet_Airways = 1
            Airline_IndiGo = 0
            Airline_Air_India = 0
            Airline_Multiple_carriers = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_GoAir = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_Jet_Airways_Business = 0
            Airline_Vistara_Premium_economy = 0
            Airline_Trujet = 0 

        elif (airline=='IndiGo'):
            Airline_Jet_Airways = 0
            Airline_IndiGo = 1
            Airline_Air_India = 0
            Airline_Multiple_carriers = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_GoAir = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_Jet_Airways_Business = 0
            Airline_Vistara_Premium_economy = 0
            Airline_Trujet = 0 

        elif (airline=='Air India'):
            Airline_Jet_Airways = 0
            Airline_IndiGo = 0
            Airline_Air_India = 1
            Airline_Multiple_carriers = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_GoAir = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_Jet_Airways_Business = 0
            Airline_Vistara_Premium_economy = 0
            Airline_Trujet = 0 
            
        elif (airline=='Multiple carriers'):
            Airline_Jet_Airways = 0
            Airline_IndiGo = 0
            Airline_Air_India = 0
            Airline_Multiple_carriers = 1
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_GoAir = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_Jet_Airways_Business = 0
            Airline_Vistara_Premium_economy = 0
            Airline_Trujet = 0
            
        elif (airline=='SpiceJet'):
            Airline_Jet_Airways = 0
            Airline_IndiGo = 0
            Airline_Air_India = 0
            Airline_Multiple_carriers = 0
            Airline_SpiceJet = 1
            Airline_Vistara = 0
            Airline_GoAir = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_Jet_Airways_Business = 0
            Airline_Vistara_Premium_economy = 0
            Airline_Trujet = 0 
            
        elif (airline=='Vistara'):
            Airline_Jet_Airways = 0
            Airline_IndiGo = 0
            Airline_Air_India = 0
            Airline_Multiple_carriers = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 1
            Airline_GoAir = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_Jet_Airways_Business = 0
            Airline_Vistara_Premium_economy = 0
            Airline_Trujet = 0 

        elif (airline=='GoAir'):
            Airline_Jet_Airways = 0
            Airline_IndiGo = 0
            Airline_Air_India = 0
            Airline_Multiple_carriers = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_GoAir = 1
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_Jet_Airways_Business = 0
            Airline_Vistara_Premium_economy = 0
            Airline_Trujet = 0 


        elif (airline=='Multiple carriers Premium economy'):
            Airline_Jet_Airways = 0
            Airline_IndiGo = 0
            Airline_Air_India = 0
            Airline_Multiple_carriers = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_GoAir = 0
            Airline_Multiple_carriers_Premium_economy = 1
            Airline_Jet_Airways_Business = 0
            Airline_Vistara_Premium_economy = 0
            Airline_Trujet = 0 

        elif (airline=='Jet Airways Business'):
            Airline_Jet_Airways = 0
            Airline_IndiGo = 0
            Airline_Air_India = 0
            Airline_Multiple_carriers = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_GoAir = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_Jet_Airways_Business = 1
            Airline_Vistara_Premium_economy = 0
            Airline_Trujet = 0 

        elif (airline=='Vistara Premium economy'):
            Airline_Jet_Airways = 0
            Airline_IndiGo = 0
            Airline_Air_India = 0
            Airline_Multiple_carriers = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_GoAir = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_Jet_Airways_Business = 0
            Airline_Vistara_Premium_economy = 1
            Airline_Trujet = 0 
            
        elif (airline=='Trujet'):
            Airline_Jet_Airways = 0
            Airline_IndiGo = 0
            Airline_Air_India = 0
            Airline_Multiple_carriers = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_GoAir = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_Jet_Airways_Business = 0
            Airline_Vistara_Premium_economy = 0
            Airline_Trujet = 1

        else:
            Airline_Jet_Airways = 0
            Airline_IndiGo = 0
            Airline_Air_India = 0
            Airline_Multiple_carriers = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_GoAir = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_Jet_Airways_Business = 0
            Airline_Vistara_Premium_economy = 0
            Airline_Trujet = 0 


        # Source
        # Banglore = 0 
        Source = request.form["Source"]
        if (Source == 'New Delhi'):
            Source_New_Delhi = 1
            Source_Kolkata = 0
            Source_Mumbai = 0
            Source_Chennai = 0

        elif (Source == 'Kolkata'):
            Source_New_Delhi = 0
            Source_Kolkata = 1
            Source_Mumbai = 0
            Source_Chennai = 0

        elif (Source == 'Mumbai'):
            Source_New_Delhi = 0
            Source_Kolkata = 0
            Source_Mumbai = 1
            Source_Chennai = 0

        elif (Source == 'Chennai'):
            Source_New_Delhi = 0
            Source_Kolkata = 0
            Source_Mumbai = 0
            Source_Chennai = 1

        else:
            Source_New_Delhi = 0
            Source_Kolkata = 0
            Source_Mumbai = 0
            Source_Chennai = 0

       

        # Destination
        # Banglore = 0 
        Destination = request.form["Destination"]
        if (Destination == 'Cochin'):
            Destination_Cochin = 1
            Destination_New_Delhi = 0
            Destination_Hyderabad = 0
            Destination_Kolkata = 0
        
        elif (Destination == 'New Delhi'):
            Destination_Cochin = 0
            Destination_New_Delhi = 1
            Destination_Hyderabad = 0
            Destination_Kolkata = 0

        elif (Destination == 'Hyderabad'):
            Destination_Cochin = 0
            Destination_New_Delhi = 0
            Destination_Hyderabad = 1
            Destination_Kolkata = 0

        elif (Destination == 'Kolkata'):
            Destination_Cochin = 0
            Destination_New_Delhi = 0
            Destination_Hyderabad = 0
            Destination_Kolkata = 1

        else:
            Destination_Cochin = 0
            Destination_New_Delhi = 0
            Destination_Hyderabad = 0
            Destination_Kolkata = 0
 
    prediction=model.predict([[
            Total_Stops,
            Additional_Info,
            Date,
            Month,
            Arrival_Hour,
            Arrival_Minute,
            Dep_Hour,
            Dep_Min,
            Duration_H,
            Duration_M,
            Airline_Air_India,
            Airline_GoAir,
            Airline_IndiGo,
            Airline_Jet_Airways,
            Airline_Jet_Airways_Business,
            Airline_Multiple_carriers,
            Airline_Multiple_carriers_Premium_economy,
            Airline_SpiceJet,
            Airline_Trujet,
            Airline_Vistara,
            Airline_Vistara_Premium_economy,
            Source_Chennai,
            Source_Kolkata,
            Source_Mumbai,
            Source_New_Delhi,
            Destination_Cochin,
            Destination_Hyderabad,
            Destination_Kolkata,
            Destination_New_Delhi
  
        ]])
          #Rounding up to 2 decimal values
    output=round(prediction[0],2)

    return redirect(url_for('predict',price=output))





if __name__ == "__main__":
    app.run(debug=True)
