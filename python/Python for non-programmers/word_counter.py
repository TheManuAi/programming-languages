text = """
Finally, after about a year, I discovered a sobering and shocking truth. I discovered that 
in spite of our enormous intake, we had not netted any profit whatever. After discovering 
that, I should have done two things. First, I should have had the sense to do what 
George Washington Carver, the Negro scientist, did when he lost forty thousand dollars 
in a bank crash-the savings of a lifetime. When someone asked him if he knew he was 
bankrupt, he replied: "Yes, I heard"-and went on with his teaching. He wiped the loss out 
of his mind so completely that he never mentioned it again. 
Here is the second thing I should have done: I should have analysed my mistakes and 
learned a lasting lesson. 
But frankly, I didn't do either one of these things. Instead, I went into a tailspin of worry. 
For months I was in a daze. I lost sleep and I lost weight. Instead of learning a lesson 
from this enormous mistake, I went right ahead and did the same thing again on a 
smaller scale! 
It is embarrassing for me to admit all this stupidity; but I discovered long ago that "it is 
easier to teach twenty what were good to be done than to be one of twenty to follow 
mine own teaching." 
How I wish that I had had the privilege of attending the George Washington High School 
here in New York and studying under Mr. Brandwine-the same teacher who taught Allen 
Saunders, of 939 Woodycrest Avenue, Bronx, New York!
"""

dic = {}
for word in text.lower().split():
    if word in dic:
        dic[word] += 1
    else:
        dic[word] = 1

print(dic)