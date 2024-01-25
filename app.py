import wonderwords
import tiktoken
from openai import AzureOpenAI
import time
from datetime import datetime
from wonderwords import RandomWord

#Generate random words
#Only used in large prompt token AOAI test
num_words = 5000
test_words = RandomWord().random_words(num_words)
comb_words = ' '.join(test_words)

#Count tokens in random words
#Only used code creation. Not used in any AOAI tests
target_model = "gpt-4"
enc = tiktoken.encoding_for_model(target_model)
num_tokens = len(enc.encode(comb_words))

#Create client
client = AzureOpenAI(
    api_key="344fcd8722804e3f96712311470472e3",
    azure_endpoint="https://mf-aoai-aitalk.openai.azure.com/",
    api_version='2023-07-01-preview',
    azure_deployment='gpt-4'
)

#start timer
now = datetime.now()
formatted_date = now.strftime("%Y-%m-%d %H:%M")
start = time.time()

#Only used in max token AOAI tests
#response = client.chat.completions.create(
    #messages=[
        #{
            #"role": "user",
            #"content": 'write a 300 word story that begins with Once upon a time and ends with The End \n\nExample 1: Once upon a time, in a faraway land, there lived a young girl named Lila. She was a curious and adventurous girl who loved to explore the world around her. One day, while wandering through the woods, she stumbled upon a hidden cave. The entrance was small, but Lila was determined to explore it. She squeezed through the narrow opening and found herself in a large cavern. The walls were covered in glittering crystals that sparkled in the dim light. Lila was amazed by the beauty of the cave and decided to explore further.\n\nAs she walked deeper into the cave, she noticed a faint glow in the distance. She followed the light and soon found herself in a large chamber. In the center of the room was a glowing orb that pulsed with a soft light. Lila approached the orb and reached out to touch it. Suddenly, she was enveloped in a bright light and felt herself being lifted off the ground.\n\nWhen the light faded, Lila found herself in a strange new world. The sky was a deep shade of purple, and the trees were made of crystal. She looked around in wonder and realized that she had been transported to a magical realm.\n\nLila spent many years exploring this new world, meeting strange creatures and having incredible adventures. But eventually, she grew homesick and decided to return to her own world. She approached the glowing orb once again and was enveloped in a bright light. When the light faded, she found herself back in the cave where she had started.\n\nLila emerged from the cave, changed forever by her incredible journey. She went on to live a long and happy life, but she never forgot the magic of that other world. And so, we come to the end of our story. The End.\n\nExample 2: Once upon a time, in the kingdom of Uriel, lived an old shoemaker named Bartolo. He was a quiet man who lived a simple life, crafting the most beautiful shoes to earn his livelihood. But Bartolo had a secret - he could weave magic into his shoes, giving them abilities far beyond any regular footwear. And so, Uriel\'s inhabitants adored his creations, no one knowing Bartolo was actually a wizard in disguise.\n\nOne gloomy evening, Bartolo noticed a young girl sobbing outside his shop. Her cloth shoes were ripped and worn, her feet bloodied from the rough city cobblestones. Bartolo\'s heart squeezed at the sight. He called out to her, promising a pair of new shoes.\n\nThe next day, Bartolo presented the girl, Lily, with enchanted dancing shoes. They would protect her feet and lead her heart to happiness. She looked up at Bartolo, her eyes wet with gratitude, and danced away, leaving a trail of soft laughter and twinkling sparkles.\n\nWeeks later, a royal proclamation announced a grand ball to choose a prince\'s bride, and Lily decided to attend. That night, her gifted shoes guided her as she danced with a grace that awoke an otherworldly charm. The prince was instantly smitten by Lily\'s uniqueness and chose her as his bride.\n\nOn their wedding, Bartolo presented a wondrous pair of shoes to Lily as a wedding gift - shoes embedded with everlasting love and compassion. Witnessing Lily\'s happiness, Bartolo felt his life had been worthwhile. He had used his magic to give joy, and in return, he was filled with contentment.\n\nYears later, after living a fulfilled magical life, Bartolo passed away. But through Lily, his magical shoes, and the little happiness they brought to this kingdom, his legacy lived on, forever woven into the fabric of Uriel\'s tales. Thus, our story concludes, until we meet again under the moonlit pages of another tale. The End.',
        #}
    #],
    #model=target_model,
    #max_tokens=450,
    #stop=['The End']
#)

#Make call to AOAI
response = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": 'write a 500 word short story',
        }
    ],
    model=target_model,
)

#end timer
end = time.time()
e2e = round(end - start,2)

#Print results
print(formatted_date + " e2e: " + str(e2e) + " prompt_tokens: " + str(response.usage.prompt_tokens) + " completion_tokens: " + str(response.usage.completion_tokens) + " total_tokens: " + str(response.usage.total_tokens))

#Only used in code creation
#print(response.model_dump_json(indent=2))