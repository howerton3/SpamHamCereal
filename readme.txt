This README file explains how the SpamHamCereal.py works and how to use it or modify it for personal needs.  It was authored by Kenneth Howerton, Sarah Gore, and Yasmeen Cherry for CSC 130, instructed by Dr. Sarami, at Fayetteville State University, April 2017. 

--Run in an IDE--

Open the file and simply run it.  The methods checkSpamHam() and menu() are already called when it is run. 

--Modification for user--

Given a .csv with compiled data:

Line 20: Change to your file name
Line 26: if your data is separated by something other than a ?;?, change it in this line to read in properly. 
Line 33: Modify the words in these two lists to be Spam or Ham based on your data. 

-Customized cereal--

Follow menu based on needs.  You can search the data from your .csv or you can enter in new data through this model.  You will have to modify the calculate_nutrition method in order to fit your needs when using something other than nutrition.  The method checkHamSpam() can be called here. 
