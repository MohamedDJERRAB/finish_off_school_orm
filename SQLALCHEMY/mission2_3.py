import sqlalchemy 
from sqlalchemy import create_engine, Table, Column, Integer, String, ForeignKey,MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import  sessionmaker

engine = create_engine('sqlite:///library_of_Alexandria.db', echo=True)

Base = declarative_base()

class books (Base):
    
    __tablename__ = 'books'
    id =Column("id",Integer, primary_key=True )
    title = Column(String)
    author=Column(String)
    description = Column(String)
    year_published=Column(Integer)

    def __repr__(self):
        return  f"{self.id}{self.title}{self.author}{self.description}{self.year_published}"




metadata = MetaData()
metadata.bind = engine
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()


book1 = books(
    id='1',
    title='Miracle Morning ', 
    author='Hal Elrod ' , 
    description='The Miracle Morning ...', 
    year_published=2016)

book2 = books (
    id='2',
    title='Le Roi Lion',
    author='Walt Disney Compagny',
    description='Au coeur de l Afrique tous les animaux de la savane se sont réunis au pied du Rocher des Lions pour célébrer la naissance de Simba, le fils du grand Mufasa. Le jeune lionceau est promis à un destin extraordinaire, un destin de roi ! Mais son maléfique oncle Scar n a qu une ambition : renverser le souverain pour prendre sa place sur le trône, et régner en tyran sur le royaume.',
    year_published=2019)

book3 = books (
    id='3',
    title='Les chemins qui montent (', 
    author='Mouloud Feraoun', 
    description='Dans Les Chemins qui montent, Mouloud Feraoun relate aux lecteurs la vie d un ensemble de personnages de caractères différents qui vivent dans un village Kabyle, pendant la guerre de libération Ce récit débute par l assassinat du personnage principal Amer, fait qui éveille la curiosité du lecteur pour découvrir les évènements qui ont signé sa mort tragique. Puis vient, avec la langue soutenue de l instituteur, son histoire d amour avec Dahbia, le deuxième personnage principal. Et au milieu de cette histoire, surgit un personnage marié et malheureux, Mokrane, qui cherche son caprice auprès d elle.', 
    year_published=1957)

book4 = books (
    id='4',
    title='PARCE QUE JE T AIME', 
    author='GUILLAUME MUSSO', 
    description='Layla, une petite fille de cinq ans, disparaît dans un centre commercial de Los Angeles. Brisés, ses parents finissent par se séparer…Cinq ans plus tard, Layla est retrouvée à l’endroit exact où on avait perdu sa trace. Elle est vivante, mais reste plongée dans un étrange mutisme.', 
    year_published=2007)

book5 = books (
    id='5',
    title='Ta deuxième vie commence quand tu comprends que tu n en as qu une', 
    author='Raphaëlle Giordano', 
    description='Camille, trente-huit ans et quart, a tout, semble-t-il, pour être heureuse. Alors pourquoi a-t-elle l impression que le bonheur lui a glissé entre les doigts ? Tout ce qu elle veut, c est retrouver le chemin de la joie et de l épanouissement. Quand Claude, routinologue, lui propose un accompagnement original pour l y aider, elle n hésite pas longtemps: elle fonce À travers des expériences étonnantes, créatives et riches de sens, elle va, pas à pas, transformer sa vie et repartir à la conquête de ses rêves...', 
    year_published=2017 )



author=input('enter the name of author:')


for book in session.query(books).filter_by(author=author):
    print(book.title)

        
# #la modification :
ID = input('Enter the ID of the book: ')
book = session.query(books).filter(id == ID)
book.description = "......................"



session.commit()
session.close()     
