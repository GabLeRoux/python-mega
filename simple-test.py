from mega import Mega

email = "juanjosalvador@netc.eu"
password = "Er0senn1n"

m = Mega.from_credentials(email, password)

m.download_from_url('https://mega.co.nz/#!wYo3AYZC!Zwi1f3ANtYwKNOc07fwuN1enOoRj4CreFouuGqi4D6Y')
