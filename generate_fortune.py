import random
import datetime
import os
from pathlib import Path

# Zodiac information
ZODIACS = {
    'Aries': '♈',
    'Taurus': '♉',
    'Gemini': '♊',
    'Cancer': '♋',
    'Leo': '♌',
    'Virgo': '♍',
    'Libra': '♎',
    'Scorpio': '♏',
    'Sagittarius': '♐',
    'Capricorn': '♑',
    'Aquarius': '♒',
    'Pisces': '♓'
}

# Phrases for fortune generation
LUCK_PHRASES = [
    'Today brings abundant luck and positive energy your way.',
    'New opportunities are on the horizon—embrace them!',
    'Positive changes are just beginning; stay open to them.',
    'Great news awaits you soon.',
    'A special encounter might brighten your day.'
]

LOVE_PHRASES = [
    'Romantic moments are in store for you.',
    'A day filled with warmth and heartfelt connections.',
    'You may encounter a meaningful connection today.',
    'Today brings an increase in love and harmony.',
    'Open your heart; it may lead to wonderful surprises.'
]

MONEY_PHRASES = [
    'Financial luck is on the rise today.',
    'A great opportunity for investment may come your way.',
    'Unexpected income could be on its way.',
    'Today brings stability to your financial situation.',
    'Fortune is smiling upon you in matters of wealth.'
]

HEALTH_PHRASES = [
    'You\'ll feel energized and full of vitality today.',
    'Today marks the beginning of a positive change for your health.',
    'Make sure to get enough rest and recharge.',
    'It\'s a good day to focus on physical activities.',
    'Take some time to enjoy fresh air and nature.'
]

COLORS = ['Red', 'Blue', 'Yellow', 'Purple', 'Green', 
         'Orange', 'Pink', 'Sky Blue', 'White', 'Black']
NUMBERS = list(range(1, 101))

def generate_fortune():
    return {
        'luck': random.choice(LUCK_PHRASES),
        'love': random.choice(LOVE_PHRASES),
        'money': random.choice(MONEY_PHRASES),
        'health': random.choice(HEALTH_PHRASES),
        'color': random.choice(COLORS),
        'number': random.choice(NUMBERS)
    }

if __name__ == "__main__":
    # Today's date
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    
    # Generate daily fortune for each zodiac sign
    for zodiac, symbol in ZODIACS.items():
        # Create folder
        folder_path = Path(zodiac)
        folder_path.mkdir(exist_ok=True)
        
        # Generate fortune
        fortune = generate_fortune()
        
        # Create markdown file
        file_path = folder_path / f'{today}.md'
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(f'# {symbol} {zodiac} Horoscope - {today}\n\n')
            f.write('## 🎯 Daily Fortune\n\n')
            f.write(f'{fortune["luck"]}\n\n')
            f.write('## 💘 Love Fortune\n\n')
            f.write(f'{fortune["love"]}\n\n')
            f.write('## 💰 Wealth Fortune\n\n')
            f.write(f'{fortune["money"]}\n\n')
            f.write('## 🌱 Health Fortune\n\n')
            f.write(f'{fortune["health"]}\n\n')
            f.write('## 🎨 Lucky Color\n\n')
            f.write(f'{fortune["color"]}\n\n')
            f.write('## 🔢 Lucky Number\n\n')
            f.write(f'{fortune["number"]}\n')
        
        os.system(f'git add "{file_path}"')
