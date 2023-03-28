import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)
    
    def test_konstruktori(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_edulliset(self):
        ret = self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(ret, 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)

        ret = self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(ret, 60)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_maukkaat(self):
        ret = self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(ret, 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)

        ret = self.kassapaate.syo_maukkaasti_kateisella(450)
        self.assertEqual(ret, 50)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_edulliset_kortilla(self):
        ret = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertTrue(ret)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.maksukortti.saldo, 1000-240)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_maukkaat_kortilla(self):
        ret = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertTrue(ret)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.maksukortti.saldo, 1000-400)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_korttimaksu_epaonnistuminen(self):
        kortti = Maksukortti(100)
        ret = self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertFalse(ret)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.maksukortti.saldo, 1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        
        ret = self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertFalse(ret)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.maksukortti.saldo, 1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kortin_lataaminen(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 100)
        
        self.assertEqual(self.maksukortti.saldo, 1100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100100)

        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -100)
        self.assertEqual(self.maksukortti.saldo, 1100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100100)
