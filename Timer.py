from nltk.tokenize.treebank import TreebankWordDetokenizer
from nltk_utils import bag_of_words, tokenize
import time
from datetime import datetime
import datetime
import pyttsx3

try:
    engine = pyttsx3.init()
except ImportError:
    print('Requested driver not found')
except RuntimeError:
    print('Driver fails to initialize')

voices = engine.getProperty('voices')
for voice in voices:
    print(voice.id)
engine.setProperty('voice',
                   'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')  # Diffrent voices = US_DAVID, GB_HAZEL, US_ZIRA
rate = engine.getProperty('rate')
engine.setProperty('rate', rate)


def speak_text_cmd(cmd):
    engine.say(cmd)
    engine.runAndWait()


def is_number(x):
    if type(x) == str:
        x = x.replace(',', '')
    try:
        float(x)
    except:
        return False
    return True

def text2int (textnum, numwords={}):
    units = [
        'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
        'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
        'sixteen', 'seventeen', 'eighteen', 'nineteen',
    ]
    tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    scales = ['hundred', 'thousand', 'million', 'billion', 'trillion']
    ordinal_words = {'first':1, 'third':3, 'fifth':5, 'eighth':8, 'ninth':9, 'twelfth':12}
    ordinal_endings = [('ieth', 'y'), ('th', '')]

    if not numwords:
        numwords['and'] = (1, 0)
        for idx, word in enumerate(units): numwords[word] = (1, idx)
        for idx, word in enumerate(tens): numwords[word] = (1, idx * 10)
        for idx, word in enumerate(scales): numwords[word] = (10 ** (idx * 3 or 2), 0)

    textnum = textnum.replace('-', ' ')

    current = result = 0
    curstring = ''
    onnumber = False
    lastunit = False
    lastscale = False

    def is_numword(x):
        if is_number(x):
            return True
        if word in numwords:
            return True
        return False

    def from_numword(x):
        if is_number(x):
            scale = 0
            increment = int(x.replace(',', ''))
            return scale, increment
        return numwords[x]

    for word in textnum.split():
        if word in ordinal_words:
            scale, increment = (1, ordinal_words[word])
            current = current * scale + increment
            if scale > 100:
                result += current
                current = 0
            onnumber = True
            lastunit = False
            lastscale = False
        else:
            for ending, replacement in ordinal_endings:
                if word.endswith(ending):
                    word = "%s%s" % (word[:-len(ending)], replacement)

            if (not is_numword(word)) or (word == 'and' and not lastscale):
                if onnumber:
                    # Flush the current number we are building
                    curstring += repr(result + current) + " "
                curstring += word + " "
                result = current = 0
                onnumber = False
                lastunit = False
                lastscale = False
            else:
                scale, increment = from_numword(word)
                onnumber = True

                if lastunit and (word not in scales):
                    # Assume this is part of a string of individual numbers to
                    # be flushed, such as a zipcode "one two three four five"
                    curstring += repr(result + current)
                    result = current = 0

                if scale > 1:
                    current = max(1, current)

                current = current * scale + increment
                if scale > 100:
                    result += current
                    current = 0

                lastscale = False
                lastunit = False
                if word in scales:
                    lastscale = True
                elif word in units:
                    lastunit = True

    if onnumber:
        curstring += repr(result + current)

    return curstring

numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
        'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
        'sixteen', 'seventeen', 'eighteen', 'nineteen']




input = search8
sentence = tokenize(input)


if "timer" in sentence:
    input = TreebankWordDetokenizer().detokenize(sentence)
    timerinput1 = text2int(input)

    timerinput = tokenize(timerinput1)
    try:

        if "hour" in timerinput or 'hours' in timerinput:
            if "hour" in timerinput:
                stringinput1 = input.split('hour', 1)[0]
                stringinput = tokenize(stringinput1)
                remove = ['second', 'seconds', 'minute', 'minutes', 'hour', 'hours',
                          'please',
                          'set', 's', 'timer', '``', '{', '}', 'text', ':', "''",
                          'a', 'for',
                          'and', 'if', 'time', 'but', 'end', 'put', 'me',
                          'my', 'will',
                          'you', 'now', 'right', 'rite', 'wright',
                          'write', 'your', 'go', 'ahead', 't', 'create', 'said', 'make', 'her', 'no', 'time', 'start']
                remove = set(remove)
                search = set(stringinput) - set(remove)
                minutes = TreebankWordDetokenizer().detokenize(search)
                hours1 = (f"{minutes}")
            if 'hours' in timerinput:
                stringinput1 = input.split('hours', 1)[0]
                stringinput = tokenize(stringinput1)
                remove = ['second', 'seconds', 'minute', 'minutes', 'hour', 'hours',
                          'please',
                          'set', 's', 'timer', '``', '{', '}', 'text', ':', "''",
                          'a', 'for',
                          'and', 'if', 'time', 'but', 'end', 'put', 'me',
                          'my', 'will',
                          'you', 'now', 'right', 'rite', 'wright',
                          'write', 'your', 'go', 'ahead', 't', 'create', 'said', 'make', 'her', 'no', 'time', 'start']
                remove = set(remove)
                search = set(stringinput) - set(remove)
                minutes = TreebankWordDetokenizer().detokenize(search)
                hours1 = (f"{minutes}")
        else:
            hours1 = '0'

        if "minutes" in timerinput or 'minute' in timerinput:
            if "hour" in timerinput:
                stringinput1 = input.split('hour', 1)[1]
                stringinput = tokenize(stringinput1)
                remove = ['second', 'seconds', 'minute', 'minutes', 'hour', 'hours',
                          'please',
                          'set', 's', 'timer', '``', '{', '}', 'text', ':', "''",
                          'a', 'for',
                          'and', 'if', 'time', 'but', 'end', 'put', 'me',
                          'my', 'will',
                          'you', 'now', 'right', 'rite', 'wright',
                          'write', 'your', 'go', 'ahead', 't', 'create', 'said', 'make', 'her', 'no', 'time', 'start']
                remove = set(remove)
                search = set(stringinput) - set(remove)
                minutes = TreebankWordDetokenizer().detokenize(search)
                minutes1 = (f"{minutes}")
            if 'hours' in timerinput:
                stringinput1 = input.split('hours', 1)[1]
                stringinput = tokenize(stringinput1)
                remove = ['second', 'seconds', 'minute', 'minutes', 'hour', 'hours',
                          'please',
                          'set', 's', 'timer', '``', '{', '}', 'text', ':', "''",
                          'a', 'for',
                          'and', 'if', 'time', 'but', 'end', 'put', 'me',
                          'my', 'will',
                          'you', 'now', 'right', 'rite', 'wright',
                          'write', 'your', 'go', 'ahead', 't', 'create', 'said', 'make', 'her', 'no', 'time', 'start']
                remove = set(remove)
                search = set(stringinput) - set(remove)
                minutes = TreebankWordDetokenizer().detokenize(search)
                minutes1 = (f"{minutes}")
            else:
                if "minute" in timerinput:
                    stringinput1 = input.split('minute', 1)[0]
                    stringinput = tokenize(stringinput1)
                    remove = ['second', 'seconds', 'minute', 'minutes', 'hour', 'hours',
                              'please',
                              'set', 's', 'timer', '``', '{', '}', 'text', ':', "''",
                              'a', 'for',
                              'and', 'if', 'time', 'but', 'end', 'put', 'me',
                              'my', 'will',
                              'you', 'now', 'right', 'rite', 'wright',
                              'write', 'your', 'go', 'ahead', 't', 'create', 'said', 'make', 'her', 'no', 'time',
                              'start']
                    remove = set(remove)
                    search = set(stringinput) - set(remove)
                    minutes = TreebankWordDetokenizer().detokenize(search)
                    minutes1 = (f"{minutes}")
                if 'minutes' in timerinput:
                    stringinput1 = input.split('minutes', 1)[0]
                    stringinput = tokenize(stringinput1)
                    remove = ['second', 'seconds', 'minute', 'minutes', 'hour', 'hours',
                              'please',
                              'set', 's', 'timer', '``', '{', '}', 'text', ':', "''",
                              'a', 'for',
                              'and', 'if', 'time', 'but', 'end', 'put', 'me',
                              'my', 'will',
                              'you', 'now', 'right', 'rite', 'wright',
                              'write', 'your', 'go', 'ahead', 't', 'create', 'said', 'make', 'her', 'no', 'time',
                              'start']
                    remove = set(remove)
                    search = set(stringinput) - set(remove)
                    minutes = TreebankWordDetokenizer().detokenize(search)
                    minutes1 = (f"{minutes}")

        else:
            minutes1 = '0'

        if "seconds" in timerinput or 'second' in timerinput:
            if "minute" in timerinput:
                stringinput1 = input.split('minute', 1)[1]
                stringinput = tokenize(stringinput1)
                remove = ['second', 'seconds', 'minute', 'minutes', 'hour', 'hours',
                          'please',
                          'set', 's', 'timer', '``', '{', '}', 'text', ':', "''",
                          'a', 'for',
                          'and', 'if', 'time', 'but', 'end', 'put', 'me',
                          'my', 'will',
                          'you', 'now', 'right', 'rite', 'wright',
                          'write', 'your', 'go', 'ahead', 't', 'create', 'said', 'make', 'her', 'no', 'time',
                          'start']
                remove = set(remove)
                search = set(stringinput) - set(remove)
                seconds = TreebankWordDetokenizer().detokenize(search)
                seconds1 = (f"{seconds}")
            if 'minutes' in timerinput:
                stringinput1 = input.split('minutes', 1)[1]
                stringinput = tokenize(stringinput1)
                remove = ['second', 'seconds', 'minute', 'minutes', 'hour', 'hours',
                          'please',
                          'set', 's', 'timer', '``', '{', '}', 'text', ':', "''",
                          'a', 'for',
                          'and', 'if', 'time', 'but', 'end', 'put', 'me',
                          'my', 'will',
                          'you', 'now', 'right', 'rite', 'wright',
                          'write', 'your', 'go', 'ahead', 't', 'create', 'said', 'make', 'her', 'no', 'time',
                          'start']
                remove = set(remove)


                search = set(stringinput) - set(remove)
                seconds = TreebankWordDetokenizer().detokenize(search)
                seconds1 = (f"{seconds}")
            else:
                if "second" in timerinput or 'seconds' in timerinput:
                    remove = ['second', 'seconds', 'minute', 'minutes', 'hour', 'hours',
                              'please',
                              'set', 's', 'timer', '``', '{', '}', 'text', ':', "''",
                              'a', 'for',
                              'and', 'if', 'time', 'but', 'end', 'put', 'me',
                              'my', 'will',
                              'you', 'now', 'right', 'rite', 'wright',
                              'write', 'your', 'go', 'ahead', 't', 'create', 'said', 'make', 'her', 'no', 'time',
                              'start']
                    remove = set(remove)
                    search = set(timerinput) - set(remove)
                    seconds = TreebankWordDetokenizer().detokenize(search)
                    seconds1 = (f"{seconds}")

        else:
            seconds1 = '0'

        if "minutes" in timerinput or 'minute' in timerinput:

            if "seconds" in timerinput or 'second' in timerinput:
                 speak_text_cmd('starting timer for ' + minutes1 + ' minutes and ' + seconds1 + ' seconds')

            if "hours" in timerinput or 'hour' in timerinput:
                speak_text_cmd(hours1 + ' hour and ' + minutes1 + ' minute timer starting now')

            else:
                speak_text_cmd('starting timer for ' + minutes1 + ' minutes')
        else:
            if "seconds" in timerinput or 'second' in timerinput:
                speak_text_cmd(seconds1 + " timer starting now")

            if "hours" in timerinput or 'hour' in timerinput:
                speak_text_cmd(hours1 + " timer starting now")

    except ValueError:
            speak_text_cmd('I didnt quite get that, can you say that again')


def countdown(h, m, s):
    total_seconds = h * 3600 + m * 60 + s
    while total_seconds > 0:
        timer = datetime.timedelta(seconds=total_seconds)

        speak_text_cmd(timer, end="\r")

        time.sleep(1)
        speak_text_cmd(total_seconds)
        total_seconds -= 1

    speak_text_cmd('timer has ended')
#data = str.split('from',1)[0]

h = hours1
m = minutes1
s = seconds1
countdown(int(h), int(m), int(s))
