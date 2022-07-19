from unittest import mock
from unittest import TestCase
import main
from datetime import datetime

class Test(TestCase):

    @mock.patch('main.input', create=True)
    def testPass(self, mocked_input):
        dateTimeObj = datetime.now()
        dateStamp = dateTimeObj.strftime('%d.%m.%Y')
        timeStamp = dateTimeObj.strftime('%H:%M')
        mocked_input.side_effect = [1, dateStamp, timeStamp]
        result = main.run()
        self.assertEqual(result, 'Finished!')
    
    @mock.patch('main.input', create=True)
    def testDate(self, mocked_input):
        dateTimeObj = datetime.now()
        dateStamp = dateTimeObj.strftime('%d-%m-%Y')
        timeStamp = dateTimeObj.strftime('%H:%M')
        mocked_input.side_effect = [1, dateStamp, timeStamp]
        result = main.run()
        self.assertRaises(ValueError)

    @mock.patch('main.input', create=True)
    def testTime(self, mocked_input):
        dateTimeObj = datetime.now()
        dateStamp = dateTimeObj.strftime('%d.%m.%Y')
        timeStamp = dateTimeObj.strftime('%H-%M')
        mocked_input.side_effect = [1, dateStamp, timeStamp]
        result = main.run()
        self.assertRaises(ValueError)
