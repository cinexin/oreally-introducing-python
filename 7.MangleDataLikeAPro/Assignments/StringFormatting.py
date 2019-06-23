'''
7.4. Write the following poem by using old-style formatting...
'''
print('My kitty cat likes %s,\nMy kitty cat likes %s,\nMy kitty cat fell on this %s\nAnd now thinks he\'s a %s' %('roast beef','ham','head','clam'))
'''
7.5. Write a form letter using new-style formatting. Save the following string as letter
'''
letter = """Dear {0[salutation]} {0[name]},\n
Thank you for your letter. We are sorry that our {0[product]} {0[verbed]} in your {0[room]}. 
Please note that it should bever be used in a {0[room]}, specially near any {0[animals]}.\n
Send us your receipt and {0[amount]} for shipping and handling.
We will send you another {0[product]} that, in our tests, is {0[percent]}% less likely to have {0[verbed]}.\n
Thank you for your support.\n
Sincerely,\n
{0[spokesman]}\n
{0[job_title]}"""
response = {'salutation': 'Mr/Ms', 
            'name': 'Totoro', 
            'product': 'Robot', 
            'verbed':'messed up', 
            'room': 'kitchen',
            'animals': 'dragon',
            'amount': 'dollars',
            'percent': 99.99,
            'spokesman': 'Migue',
            'job_title': 'CEO'}
print(letter.format(response))