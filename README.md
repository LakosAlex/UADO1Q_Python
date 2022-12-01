# UADO1Q_Python
Beadandó - UADO1Q

A program a felahsználó által megadott adatokat képes eltárolni külső adatbázisban (regisztráció), illetve szükség esetén képes
meghívni azokat (login ellenőrzés). Képes véletlenszerű felhasználói adatokat generálni a regisztráció során.

main modul : createLoginGui(), createRegistrationGUI(), generateFakeData(), emptyComponents(), createDataOutputGUI(), fillTreeView()
             saveTreeView()
DB modul: connectToDB(), checkLogin(), insertUserIntoDB(), getAllUsers()
HASH modul: getHashedPassword()
User modul: UserEntity class, UserLoginDto class, UserTreeViewDto class