import unittest
import workflows

class ContractTests(unittest.TestCase):
    def test_net_00(self):
        self.assertEqual(workflows.net(*[[('c', 1000), ('r', 0)]]), 1000)

    def test_net_01(self):
        self.assertEqual(workflows.net(*[[('c', 1001), ('c', 1001), ('r', -1), ('r', -1)]]), 1000)

    def test_net_02(self):
        self.assertEqual(workflows.net(*[[('c', 1002), ('c', 1002), ('c', 1002), ('r', -2)]]), 1000)

    def test_net_03(self):
        self.assertEqual(workflows.net(*[[('c', 1003), ('r', -3), ('r', -3)]]), 1000)

    def test_net_04(self):
        self.assertEqual(workflows.net(*[[('c', 1004), ('c', 1004), ('r', -4)]]), 1000)

    def test_net_05(self):
        self.assertEqual(workflows.net(*[[('c', 1005), ('c', 1005), ('c', 1005), ('r', -5), ('r', -5)]]), 1000)

    def test_net_06(self):
        self.assertEqual(workflows.net(*[[('c', 1006), ('r', -6)]]), 1000)

    def test_net_07(self):
        self.assertEqual(workflows.net(*[[('c', 1007), ('c', 1007), ('r', -7), ('r', -7)]]), 1000)

    def test_net_08(self):
        self.assertEqual(workflows.net(*[[('c', 1008), ('c', 1008), ('c', 1008), ('r', -8)]]), 1000)

    def test_net_09(self):
        self.assertEqual(workflows.net(*[[('c', 1009), ('r', -9), ('r', -9)]]), 1000)

    def test_net_10(self):
        self.assertEqual(workflows.net(*[[('c', 1010), ('c', 1010), ('r', -10)]]), 1000)

    def test_net_11(self):
        self.assertEqual(workflows.net(*[[('c', 1011), ('c', 1011), ('c', 1011), ('r', -11), ('r', -11)]]), 1000)

    def test_net_12(self):
        self.assertEqual(workflows.net(*[[('c', 1012), ('r', -12)]]), 1000)

    def test_net_13(self):
        self.assertEqual(workflows.net(*[[('c', 1013), ('c', 1013), ('r', -13), ('r', -13)]]), 1000)

    def test_net_14(self):
        self.assertEqual(workflows.net(*[[('c', 1014), ('c', 1014), ('c', 1014), ('r', -14)]]), 1000)

    def test_net_15(self):
        self.assertEqual(workflows.net(*[[('c', 1015), ('r', -15), ('r', -15)]]), 1000)

    def test_net_16(self):
        self.assertEqual(workflows.net(*[[('c', 1016), ('c', 1016), ('r', -16)]]), 1000)

    def test_net_17(self):
        self.assertEqual(workflows.net(*[[('c', 1017), ('c', 1017), ('c', 1017), ('r', -17), ('r', -17)]]), 1000)

    def test_net_18(self):
        self.assertEqual(workflows.net(*[[('c', 1018), ('r', -18)]]), 1000)

    def test_net_19(self):
        self.assertEqual(workflows.net(*[[('c', 1019), ('c', 1019), ('r', -19), ('r', -19)]]), 1000)

    def test_state_00(self):
        self.assertEqual(workflows.state(*[100, 0]), 'captured')

    def test_state_01(self):
        self.assertEqual(workflows.state(*[101, 2]), 'partial')

    def test_state_02(self):
        self.assertEqual(workflows.state(*[102, 102]), 'refunded')

    def test_state_03(self):
        self.assertEqual(workflows.state(*[103, 104]), 'invalid')

    def test_state_04(self):
        self.assertEqual(workflows.state(*[104, -1]), 'invalid')

    def test_state_05(self):
        self.assertEqual(workflows.state(*[105, 0]), 'captured')

    def test_state_06(self):
        self.assertEqual(workflows.state(*[106, 7]), 'partial')

    def test_state_07(self):
        self.assertEqual(workflows.state(*[107, 107]), 'refunded')

    def test_state_08(self):
        self.assertEqual(workflows.state(*[108, 109]), 'invalid')

    def test_state_09(self):
        self.assertEqual(workflows.state(*[109, -1]), 'invalid')

    def test_state_10(self):
        self.assertEqual(workflows.state(*[110, 0]), 'captured')

    def test_state_11(self):
        self.assertEqual(workflows.state(*[111, 12]), 'partial')

    def test_state_12(self):
        self.assertEqual(workflows.state(*[112, 112]), 'refunded')

    def test_state_13(self):
        self.assertEqual(workflows.state(*[113, 114]), 'invalid')

    def test_state_14(self):
        self.assertEqual(workflows.state(*[114, -1]), 'invalid')

    def test_state_15(self):
        self.assertEqual(workflows.state(*[115, 0]), 'captured')

    def test_state_16(self):
        self.assertEqual(workflows.state(*[116, 17]), 'partial')

    def test_state_17(self):
        self.assertEqual(workflows.state(*[117, 117]), 'refunded')

    def test_state_18(self):
        self.assertEqual(workflows.state(*[118, 119]), 'invalid')

    def test_state_19(self):
        self.assertEqual(workflows.state(*[119, -1]), 'invalid')

    def test_match_00(self):
        self.assertEqual(workflows.match(*['PAY-0', 100, []]), 'missing')

    def test_match_01(self):
        self.assertEqual(workflows.match(*['PAY-1', 101, [('pay1', 40), ('PAY-1', 61)]]), 'matched')

    def test_match_02(self):
        self.assertEqual(workflows.match(*['PAY-2', 102, [('pay2', 40), ('PAY-2', 63)]]), 'excess')

    def test_match_03(self):
        self.assertEqual(workflows.match(*['PAY-3', 103, [('pay3', 40), ('PAY-3', 62)]]), 'short')

    def test_match_04(self):
        self.assertEqual(workflows.match(*['PAY-4', 104, []]), 'missing')

    def test_match_05(self):
        self.assertEqual(workflows.match(*['PAY-5', 105, [('pay5', 40), ('PAY-5', 66)]]), 'excess')

    def test_match_06(self):
        self.assertEqual(workflows.match(*['PAY-6', 106, [('pay6', 40), ('PAY-6', 65)]]), 'short')

    def test_match_07(self):
        self.assertEqual(workflows.match(*['PAY-7', 107, [('pay7', 40), ('PAY-7', 67)]]), 'matched')

    def test_match_08(self):
        self.assertEqual(workflows.match(*['PAY-8', 108, []]), 'missing')

    def test_match_09(self):
        self.assertEqual(workflows.match(*['PAY-9', 109, [('pay9', 40), ('PAY-9', 68)]]), 'short')

    def test_match_10(self):
        self.assertEqual(workflows.match(*['PAY-10', 110, [('pay10', 40), ('PAY-10', 70)]]), 'matched')

    def test_match_11(self):
        self.assertEqual(workflows.match(*['PAY-11', 111, [('pay11', 40), ('PAY-11', 72)]]), 'excess')

    def test_match_12(self):
        self.assertEqual(workflows.match(*['PAY-12', 112, []]), 'missing')

    def test_match_13(self):
        self.assertEqual(workflows.match(*['PAY-13', 113, [('pay13', 40), ('PAY-13', 73)]]), 'matched')

    def test_match_14(self):
        self.assertEqual(workflows.match(*['PAY-14', 114, [('pay14', 40), ('PAY-14', 75)]]), 'excess')

    def test_match_15(self):
        self.assertEqual(workflows.match(*['PAY-15', 115, [('pay15', 40), ('PAY-15', 74)]]), 'short')

    def test_match_16(self):
        self.assertEqual(workflows.match(*['PAY-16', 116, []]), 'missing')

    def test_match_17(self):
        self.assertEqual(workflows.match(*['PAY-17', 117, [('pay17', 40), ('PAY-17', 78)]]), 'excess')

    def test_match_18(self):
        self.assertEqual(workflows.match(*['PAY-18', 118, [('pay18', 40), ('PAY-18', 77)]]), 'short')

    def test_match_19(self):
        self.assertEqual(workflows.match(*['PAY-19', 119, [('pay19', 40), ('PAY-19', 79)]]), 'matched')
