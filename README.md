# 💰Currency Arbitrage Detector  
Currency Exchange can be inefficient by simply transferring money from one currency to another you could end up paying more by going from source to target. Than if you went through a set path, giving you more for your money.  
   
Arbitrage is when there is a negative cycle. A negative cycle is when the exchange rates of different currencies multiply and give you more money than you put in. For example: USD -> EUR = 1.1, EUR -> AUD = 1.2, AUD -> USD = 1.1, If you convert 1 USD through this cycle 1 x 1.1 = 1.1, 1.1 x 1.2 = 1.32, 1.32 x 1.1 = 1.452. You end up with 1.452 USD although you started with 1    
  
I chose Floyd-Warshall as it is a simple and easy to understand algorithm, which finds the shortest path between all currencies. 
It allows easy detection of arbitrage as the currency rate to itself will be less than 1 if there is arbitrage. 
Although Floyd-warshall is less efficient at O(n^3) and Bellman-ford is O(n x m) this will be fine for my case as we aren’t using a large dataset of currencies which made it negligible.  
  
I have used real time api data, using freecurrencyapi.com, which gives live currencies. As well as the option for user inputted data.  

   
## 📖Language:  
Python  
   
## 📱Features:  
Real Time api currencies  
Manual input  
  
## ✍️Summary + What I have learned  
When no arbitrage exists, Best path can be achieved using floydwarshall algorithm, in both test cases and through the use of live api currencies.   
  
The detection of arbitrage cycles is achieved through floydwarshall as well, with the negative cycle able to be found and displayed.   
  
My solution is easy to use, and is quick for smaller datasets. My code is robust and is easily available for use.  
  
Possible improvements would be finding the best arbitrage cycle, ive noticed in some test cases with arbitrage, that my systems detects arbitrage and finds a negative cycle. 
But doesn’t find the most efficient and highest profit cycle. Thus that would be a possible improvement.

## Explainatory Video  
https://github.com/user-attachments/assets/911dce44-8194-42de-a626-74c154f41ba5



