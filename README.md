<h1> Music Industry during Catastrophic Economic Events </h1>
<p>What music features do fans of the billboard top 100 songs listen to more during recessions vs. during economic growth and stagnation? Based on these features, can we predict whether a song was popular during a recession?</p>

<h2>Data</h2>
<p>The Billboard Hot 100 lists the top trending songs each week. After running into several issues with scraping the Spotify website and the overall tax on my small machine, that data was outsourced. For this paper, Sean Miller gathered data from the Billboard Hot 100 from 1958 to 2021. He has gathered the Hot 100 songs and a dataset with the song features from Spotify's API.</p>

<h3>Datasets</h3>
<ul>
 <li> Billboard Hot 100 from 1960 to 2021</li>
 <li> Hot 100 song features dataframe by kcseanmiller on data.world</li>
 <li> Real Gross Domestic Product from fred.stlouisfed.org/series/GPDC1</li>
 </ul>

<h2>Conclusion</h2>
<br>
<p>With the linear regression model, I extracted the coefficients of each of the variables to develop a stochastic equation. If the songs had the features listed within the stochastic equation, they would add or subtract the coefficient times the recorded value from the recession score. If the score was more significant than 0.5, the model predicted the song was recorded during a recession. Otherwise, it was recorded as not being in a recession. The model's accuracy turned out to do very well, with a score of 96.4% accurate predictions across the model with as little as one fold.</p>
<p>In conclusion, danceability, acoustics, speechiness, energy, instrumentals, and liveness predicted the catastrophic economic events while these songs were on the Billboard Hot 100 list. With this model, in the following data practicum, I will develop a predictor script to predict future songs and their performance during a recession. I have areas in which to expand my machine learning skills, and I will take classes next year to handle significant data issues. </p>

<h2>Noteable Results</h2>
<br>
<p>I was surprised to find that "liveness" was a noteable indicator of songs that tracked during recessions. Live songs that were listed on the Billboard hot 100 list had a greater chance of being popular during a recession. This may be due to the costs associated with attending live events as well as the public policies that inhibited them from attending crowded events as seen during the COVID-19 pandemic.</p>
