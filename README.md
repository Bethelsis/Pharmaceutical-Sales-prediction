## Pharmaceutical-Sales-prediction

### Objective <br>

The main objective is to build and serve an end-to-end product that forecast sales in all <br>
Rossmann Pharmaceuticals stores across several cities, six weeks ahead of time. 

### Data <br>
The data used can be found [here](https://www.kaggle.com/c/rossmann-store-sales/data).

**Sales**: the turnover for any given day (target variable). <br>
**Customers**: the number of customers on a given day. <br>
**Open**: an indicator for whether the store was open: 0 = closed, 1 = open. <br>
**Promo**: indicates whether a store is running a promo on that day. <br>
**StateHoliday**: indicates a state holiday. Normally all stores, with few exceptions, are closed on state holidays. <br>
**SchoolHoliday**: indicates if the (Store, Date) was affected by the closure of public schools. <br>
**Store**: a unique Id for each store <br>
**StoreType**: differentiates between 4 different store models: a, b, c, d <br>
**Assortment**: describes an assortment level: a = basic, b = extra, c = extended <br>
**CompetitionDistance**: distance in meters to the nearest competitor store <br>
**CompetitionOpenSince[Month/Year]**: gives the approximate year and month of the time the nearest competitor was opened <br>
**Promo2**: Promo2 is a continuing a promotion for some -stores: 0 = store is not participating, 1 = store is participating <br>
**Promo2Since[Year/Week]**: describes the year and calendar week when the store started participating in Promo2 <br>
**PromoInterval**: describes the consecutive intervals Promo2 is started, naming the months the promotion is started.  <br>E.g. "Feb,May,Aug,Nov" means each round starts in February, May, August, November of any given year for that store

### This project is divided into four main sections:<br>

**Time series analysis:** Examining existing records for trends and seasonality and drawing conclusions based on the findings.

**Regression:** predicting sales over the next six weeks across various stores.

**Model Deployment:** utilizing streamlit, a python package for web-app development.

**Hosting:** Making the web app available to the public.



