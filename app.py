import streamlit as st

def main():
    st.set_page_config(page_title="Match Predictor", page_icon=":soccer:")
    st.header("Match Predictor")

    team_players = {

        "AFC Bournemouth": [
            {"name": "Adams, Tyler Shaan", "position": "Midfielder"},
            {"name": "Adli, Amine", "position": "Midfielder"},
            {"name": "Araujo Zuniga, Julian Vicente", "position": "Defender"},
            {"name": "Bevan, Owen Lucas", "position": "Defender"},
            {"name": "Brooks, David Robert", "position": "Forward"},
            {"name": "Christie, Ryan", "position": "Midfielder"},
            {"name": "Cook, Lewis John", "position": "Midfielder"},
            {"name": "De Lima Barbosa, Francisco Evanilson", "position": "Midfielder"},
            {"name": "Dennis, William Jonathon", "position": "Goalkeeper"},
            {"name": "Diakite, Bafode", "position": "Defender"},
            {"name": "Hill, James", "position": "Defender"},
            {"name": "Kluivert, Justin Dean", "position": "Forward"},
            {"name": "Petrovic, Djorde", "position": "Goalkeeper"},
            {"name": "Sadi, Dominic Wadi", "position": "Forward"},
            {"name": "Scott, Alex Jay", "position": "Midfielder"},
            {"name": "Semenyo, Antoine Serlom", "position": "Forward"},
            {"name": "Senesi Baron, Marcos Nicolas", "position": "Defender"},
            {"name": "Smith, Adam James", "position": "Defender"},
            {"name": "Tavernier, Marcus Joseph", "position": "Midfielder"},
            {"name": "Truffert, Adrien Lillan Gaetan", "position": "Defender"},
            {"name": "Unal, Enes", "position": "Forward"}
        ],
        
        "Arsenal": [
            {"name": "Arrizabalaga Revuelta, Kepa", "position": "Goalkeeper"},
            {"name": "Calafiori, Riccardo", "position": "Defender"},
            {"name": "Dos Santos Magalhães, Gabriel", "position": "Defender"},
            {"name": "Eze, Eberechi Oluchi", "position": "Midfielder"},
            {"name": "Fernando De Jesus, Gabriel", "position": "Forward"},
            {"name": "Gyökeres, Viktor Einar", "position": "Forward"},
            {"name": "Havertz, Kai", "position": "Midfielder"},
            {"name": "Hincapie Reyna, Piero Martin", "position": "Defender"},
            {"name": "Madueke, Chukwunonso Azuka Tristan", "position": "Forward"},
            {"name": "Merino Zazon, Mikel", "position": "Midfielder"},
            {"name": "Norgaard, Christian", "position": "Midfielder"},
            {"name": "Odegaard, Martin", "position": "Midfielder"},
            {"name": "Raya Martin, David", "position": "Goalkeeper"},
            {"name": "Rice, Declan", "position": "Midfielder"},
            {"name": "Saka, Bukayo", "position": "Forward"},
            {"name": "Saliba, William", "position": "Defender"},
            {"name": "Teodoro Martinelli Silva, Gabriel", "position": "Forward"},
            {"name": "Timber, Jurrien", "position": "Defender"},
            {"name": "Trossard, Leandro", "position": "Forward"},
            {"name": "White, Benjamin", "position": "Defender"},
            {"name": "Zubimendi Ibáñez, Martín", "position": "Midfielder"}
        ],
        
        "Aston Villa": [
            {"name": "Barkley, Ross", "position": "Midfielder"},
            {"name": "Bizot, Marco", "position": "Goalkeeper"},
            {"name": "Buendia Stati, Emiliano", "position": "Midfielder"},
            {"name": "Cash, Matthew Stuart", "position": "Defender"},
            {"name": "Digne, Lucas", "position": "Defender"},
            {"name": "Elliott, Harvey Daniel James", "position": "Midfielder"},
            {"name": "Francisco Torres, Pau", "position": "Defender"},
            {"name": "Garcia Robledo, Andres", "position": "Defender"},
            {"name": "Guessand, Evann Ludovic Vidjannagni", "position": "Forward"},
            {"name": "Kamara, Boubacar Bernard", "position": "Midfielder"},
            {"name": "Konsa, Ezri Ngoyo", "position": "Defender"},
            {"name": "Maatsen, Ian Ethan", "position": "Defender"},
            {"name": "Malen, Donyell", "position": "Forward"},
            {"name": "Martinez Romero, Damian Emiliano", "position": "Goalkeeper"},
            {"name": "McGinn, John", "position": "Midfielder"},
            {"name": "Mings, Tyrone Deon", "position": "Defender"},
            {"name": "Mvom Onana, Amadou Ba Z", "position": "Midfielder"},
            {"name": "Nilsson Lindelof, Victor Jorgen", "position": "Defender"},
            {"name": "Rogers, Morgan Elliot", "position": "Midfielder"},
            {"name": "Sancho, Jadon Malik", "position": "Forward"},
            {"name": "Tielemans, Youri Marion", "position": "Midfielder"},
            {"name": "Watkins, Oliver George Arthur", "position": "Forward"}
        ],
        
        "Brentford": [
            {"name": "Adedokun, Valentino Mayowa", "position": "Forward"},
            {"name": "Ajer, Kristoffer Vassbakk", "position": "Defender"},
            {"name": "Balcombe, Ellery Ronald", "position": "Goalkeeper"},
            {"name": "Collins, Nathan", "position": "Defender"},
            {"name": "Cox, Matthew Aidan", "position": "Goalkeeper"},
            {"name": "Damsgaard, Mikkel Krogh", "position": "Midfielder"},
            {"name": "Freitas Gouveia De Carvalho, Fabio Leandro", "position": "Forward"},
            {"name": "Harris, Myles Spencer", "position": "Midfielder"},
            {"name": "Henderson, Jordan Brian", "position": "Midfielder"},
            {"name": "Henry, Rico", "position": "Defender"},
            {"name": "Hickey, Aaron Buchanan", "position": "Defender"},
            {"name": "Janelt, Vitaly", "position": "Midfielder"},
            {"name": "Jensen, Mathias", "position": "Midfielder"},
            {"name": "Kelleher, Caoimhin Odhran", "position": "Goalkeeper"},
            {"name": "Lewis-Potter, Keane William", "position": "Forward"},
            {"name": "Maghoma, Edmond-Paris", "position": "Midfielder"},
            {"name": "Nascimento Rodrigues, Igor Thiago", "position": "Midfielder"},
            {"name": "Nelson, Reiss", "position": "Forward"},
            {"name": "Onyeka, Ogochukwu Frank", "position": "Midfielder"},
            {"name": "Ouattara, Dango Aboubacar Faissal", "position": "Forward"},
            {"name": "Pinnock, Ethan Rupert", "position": "Defender"},
            {"name": "Schade, Kevin", "position": "Forward"},
            {"name": "Valdimarsson, Hakon Rafn", "position": "Goalkeeper"},
            {"name": "Van Den Berg, Sepp", "position": "Defender"}
        ],
        
        "Brighton & Hove Albion": [
            {"name": "Ayari, Yasin", "position": "Midfielder"},
            {"name": "Boscagli, Olivier", "position": "Defender"},
            {"name": "Coppola, Diego", "position": "Defender"},
            {"name": "De Cuyper, Maxim Peter", "position": "Defender"},
            {"name": "Dunk, Lewis Carl", "position": "Defender"},
            {"name": "Gomez Amarilla, Diego Alexander", "position": "Forward"},
            {"name": "Kadioglu, Ferdi Erenay", "position": "Defender"},
            {"name": "March, Soloman Benjamin", "position": "Midfielder"},
            {"name": "McGill, Thomas Peter Wayne", "position": "Goalkeeper"},
            {"name": "Milner, James Phillips", "position": "Midfielder"},
            {"name": "Mitoma, Kaoru", "position": "Forward"},
            {"name": "Rushworth, Carl Andrew", "position": "Goalkeeper"},
            {"name": "Rutter, Georginio", "position": "Forward"},
            {"name": "Steele, Jason Sean", "position": "Goalkeeper"},
            {"name": "Van Hecke, Jan Paul", "position": "Defender"},
            {"name": "Veltman, Joel Ivo", "position": "Defender"},
            {"name": "Verbruggen, Bart", "position": "Goalkeeper"},
            {"name": "Webster, Adam Harry", "position": "Defender"},
            {"name": "Welbeck, Daniel", "position": "Forward"},
            {"name": "Wieffer, Mats Henrik Berne", "position": "Midfielder"}
        ],
        
        "Burnley": [
            {"name": "Anthony, Jaidon", "position": "Forward"},
            {"name": "Barnes, Ashley", "position": "Forward"},
            {"name": "Broja, Armando", "position": "Forward"},
            {"name": "Cullen, Joshua Jon", "position": "Midfielder"},
            {"name": "Dubravka, Martin", "position": "Goalkeeper"},
            {"name": "Edwards, Marcus", "position": "Forward"},
            {"name": "Ekdal, Hjalmar", "position": "Defender"},
            {"name": "Estève, Maxime", "position": "Defender"},
            {"name": "Flemming, Zian", "position": "Midfielder"},
            {"name": "Foster, Lyle Brent", "position": "Forward"},
            {"name": "Hartman, Quilindschy", "position": "Defender"},
            {"name": "Hladký, Vaclav", "position": "Goalkeeper"},
            {"name": "Humphreys, Bashir", "position": "Defender"},
            {"name": "Larsen, Jacob Bruun", "position": "Forward"},
            {"name": "Laurent, Joshua Ishaele Jacob-Heron", "position": "Defender"},
            {"name": "Mejbri, Hannibal", "position": "Midfielder"},
            {"name": "Morris Luis, Florentina Ibrain", "position": "Midfielder"},
            {"name": "Pires Silva, Lucas", "position": "Forward"},
            {"name": "Roberts, Connor", "position": "Defender"},
            {"name": "Sonne, Oliver", "position": "Defender"},
            {"name": "Tchaouna, Loum", "position": "Forward"},
            {"name": "Tresor Ndayishimiye, Mike", "position": "Midfielder"},
            {"name": "Tuanzebe, Axel", "position": "Defender"},
            {"name": "Walker, Kyle Andrew", "position": "Defender"},
            {"name": "Worrall, Joseph Adrian", "position": "Defender"}
        ],
        
        "Chelsea": [
            {"name": "Acheampong, Josh", "position": "Defender"},
            {"name": "Adarabioyo, Tosin", "position": "Defender"},
            {"name": "Badiashile Mukinayi, Benoit Ntambue", "position": "Defender"},
            {"name": "Buonanotte, Facundo", "position": "Midfielder"},
            {"name": "Caicedo Corozo, Moises Isaac", "position": "Midfielder"},
            {"name": "Chalobah, Trevoh", "position": "Defender"},
            {"name": "Cucurella Saseta, Marc", "position": "Defender"},
            {"name": "Delap, Liam", "position": "Forward"},
            {"name": "Essugo, Dario", "position": "Midfielder"},
            {"name": "Estevão", "position": "Forward"},
            {"name": "Fernandez, Enzo Jeremias", "position": "Midfielder"},
            {"name": "Fofana, Wesley Tidjan", "position": "Defender"},
            {"name": "Garnacho, Alejandro", "position": "Forward"},
            {"name": "George, Tyreek", "position": "Midfielder"},
            {"name": "Gittens, Jamie", "position": "Midfielder"},
            {"name": "Gusto, Malo", "position": "Defender"},
            {"name": "Hato, Jorrel", "position": "Defender"},
            {"name": "James, Reece", "position": "Defender"},
            {"name": "Jorgensen, Filip", "position": "Goalkeeper"},
            {"name": "Lavia, Romeo", "position": "Midfielder"},
            {"name": "Neto Lomba, Pedro", "position": "Goalkeeper"},
            {"name": "Palmer, Cole", "position": "Midfielder"},
            {"name": "Pedro Junqueira De Jesus, Joao", "position": "Forward"},
            {"name": "Sanchez, Robert Lynch", "position": "Goalkeeper"},
            {"name": "Slonina, Gabriel", "position": "Goalkeeper"}
        ],
        
        "Crystal Palace": [
            {"name": "Adaramola, Tayo", "position": "Defender"},
            {"name": "Andersen, Joachim", "position": "Defender"},
            {"name": "Ayew, Jordan", "position": "Forward"},
            {"name": "Doucouré, Cheick", "position": "Midfielder"},
            {"name": "Edouard, Odsonne", "position": "Forward"},
            {"name": "Eze, Eberechi Oluchi", "position": "Midfielder"},
            {"name": "Guéhi, Marc", "position": "Defender"},
            {"name": "Henderson, Dean", "position": "Goalkeeper"},
            {"name": "Hughes, Will", "position": "Midfielder"},
            {"name": "Johnstone, Sam", "position": "Goalkeeper"},
            {"name": "Lerma, Jefferson", "position": "Midfielder"},
            {"name": "Mateta, Jean-Philippe", "position": "Forward"},
            {"name": "Mitchell, Tyrick", "position": "Defender"},
            {"name": "Munoz, Daniel", "position": "Defender"},
            {"name": "Olise, Michael", "position": "Forward"},
            {"name": "Richards, Chris", "position": "Defender"},
            {"name": "Uche, Christantus", "position": "Midfielder"},
            {"name": "Ward, Joel", "position": "Defender"}
        ],
        
        "Everton": [
            {"name": "Alli, Dele", "position": "Midfielder"},
            {"name": "Danjuma Groeneveld, Arnaut", "position": "Forward"},
            {"name": "Doucouré, Abdoulaye", "position": "Midfielder"},
            {"name": "Grealish, Jack", "position": "Forward"},
            {"name": "Gueye, Idrissa", "position": "Midfielder"},
            {"name": "Harrison, Jack", "position": "Midfielder"},
            {"name": "Keane, Michael", "position": "Defender"},
            {"name": "Lonergan, Andy", "position": "Goalkeeper"},
            {"name": "McNeil, Dwight", "position": "Midfielder"},
            {"name": "Mykolenko, Vitaliy", "position": "Defender"},
            {"name": "Ndiaye, Iliman", "position": "Forward"},
            {"name": "Onana, Amadou", "position": "Midfielder"},
            {"name": "Patterson, Nathan", "position": "Defender"},
            {"name": "Pickford, Jordan", "position": "Goalkeeper"},
            {"name": "Tarkowski, James", "position": "Defender"},
            {"name": "Warrington, Lewis", "position": "Midfielder"},
            {"name": "Young, Ashley", "position": "Defender"}
        ],
        
        "Fulham": [
            {"name": "Adarabioyo, Tosin", "position": "Defender"},
            {"name": "Ait-Nouri, Rayan", "position": "Defender"},
            {"name": "Bassey, Calvin", "position": "Defender"},
            {"name": "Cairney, Tom", "position": "Midfielder"},
            {"name": "Decordova-Reid, Bobby", "position": "Forward"},
            {"name": "Diop, Issa", "position": "Defender"},
            {"name": "Frimpong, Jeremie", "position": "Defender"},
            {"name": "Gomez, Joao", "position": "Midfielder"},
            {"name": "Iwobi, Alex", "position": "Midfielder"},
            {"name": "Jimenez, Raul", "position": "Forward"},
            {"name": "Leno, Bernd", "position": "Goalkeeper"},
            {"name": "Lukic, Sasa", "position": "Midfielder"},
            {"name": "Muniz Carvalho, Rodrigo", "position": "Forward"},
            {"name": "Palhinha Goncalves, Joao Maria", "position": "Midfielder"},
            {"name": "Pereira, Andreas", "position": "Midfielder"},
            {"name": "Ream, Tim", "position": "Defender"},
            {"name": "Robinson, Antonee", "position": "Defender"},
            {"name": "Rodak, Marek", "position": "Goalkeeper"},
            {"name": "Samuel Chukwueze, Samuel", "position": "Forward"},
            {"name": "Tete, Kenny", "position": "Defender"},
            {"name": "Willian", "position": "Forward"},
            {"name": "Wilson, Harry", "position": "Forward"}
        ],
        
        "Leeds United": [
            {"name": "Aaronson, Brenden", "position": "Midfielder"},
            {"name": "Adams, Tyler", "position": "Midfielder"},
            {"name": "Firpo, Junior", "position": "Defender"},
            {"name": "Gelhardt, Joe", "position": "Forward"},
            {"name": "Gray, Archie", "position": "Midfielder"},
            {"name": "Harrison, Jack", "position": "Midfielder"},
            {"name": "James, Daniel", "position": "Forward"},
            {"name": "Kristensen, Rasmus", "position": "Defender"},
            {"name": "Meslier, Illan", "position": "Goalkeeper"},
            {"name": "Nmecha, Lukas", "position": "Midfielder"},
            {"name": "Perkins, Sonny", "position": "Forward"},
            {"name": "Rutter, Georginio", "position": "Forward"},
            {"name": "Sinisterra, Luis", "position": "Forward"},
            {"name": "Struijk, Pascal", "position": "Defender"},
            {"name": "Summerville, Crysencio", "position": "Forward"}
        ],
        
        "Liverpool": [
            {"name": "Alisson Becker", "position": "Goalkeeper"},
            {"name": "Alexander-Arnold, Trent", "position": "Defender"},
            {"name": "Bradley, Conor", "position": "Defender"},
            {"name": "Chiesa, Federico", "position": "Forward"},
            {"name": "Dorgu, Patrick Chinazaekpere", "position": "Defender"},
            {"name": "Endo, Wataru", "position": "Midfielder"},
            {"name": "Ekitiké, Hugo", "position": "Forward"},
            {"name": "Gakpo, Cody", "position": "Forward"},
            {"name": "Gomez, Joe", "position": "Defender"},
            {"name": "Jones, Curtis", "position": "Midfielder"},
            {"name": "Kelleher, Caoimhin Odhran", "position": "Goalkeeper"},
            {"name": "Kerkez, Milos", "position": "Defender"},
            {"name": "Konaté, Ibrahima", "position": "Defender"},
            {"name": "Leoni, Giovanni", "position": "Midfielder"},
            {"name": "Mac Allister, Alexis", "position": "Midfielder"},
            {"name": "Robertson, Andy", "position": "Defender"},
            {"name": "Salah, Mohamed", "position": "Forward"},
            {"name": "Szoboszlai, Dominik", "position": "Midfielder"},
            {"name": "Van Dijk, Virgil", "position": "Defender"},
            {"name": "Wirtz, Florian", "position": "Midfielder"}
        ],
        
        "Manchester City": [
            {"name": "Alvarez, Julian", "position": "Forward"},
            {"name": "Aké, Nathan", "position": "Defender"},
            {"name": "Bettinelli, Marcus", "position": "Goalkeeper"},
            {"name": "Dias, Rúben", "position": "Defender"},
            {"name": "Donnarumma, Gianluigi", "position": "Goalkeeper"},
            {"name": "Doku, Jeremy", "position": "Forward"},
            {"name": "Foden, Phil", "position": "Midfielder"},
            {"name": "Haaland, Erling", "position": "Forward"},
            {"name": "Ortega Moreno, Stefan", "position": "Goalkeeper"},
            {"name": "Rodri", "position": "Midfielder"},
            {"name": "Trafford, James", "position": "Goalkeeper"}
        ],
        
        "Manchester United": [
            {"name": "Bayindir, Altay", "position": "Goalkeeper"},
            {"name": "Bennett, Rhys", "position": "Defender"},
            {"name": "Bruno Fernandes, Bruno", "position": "Midfielder"},
            {"name": "Casemiro", "position": "Midfielder"},
            {"name": "Cunha, Matheus", "position": "Forward"},
            {"name": "Dalot, Diogo", "position": "Defender"},
            {"name": "De Ligt, Matthijs", "position": "Defender"},
            {"name": "Heaton, Tom", "position": "Goalkeeper"},
            {"name": "Lammens, Senne", "position": "Goalkeeper"},
            {"name": "Lisandro Martinez, Lisandro", "position": "Defender"},
            {"name": "Luke Shaw, Luke", "position": "Defender"},
            {"name": "Maguire, Harry", "position": "Defender"},
            {"name": "Malacia, Tyrell", "position": "Defender"},
            {"name": "Mazraoui, Noussair", "position": "Defender"},
            {"name": "Mee, Dermot", "position": "Midfielder"},
            {"name": "Mount, Mason", "position": "Midfielder"},
            {"name": "Mbeumo, Bryan", "position": "Forward"},
            {"name": "Sesko, Benjamin", "position": "Forward"},
            {"name": "Ugarte, Manuel", "position": "Midfielder"},
            {"name": "Zirkzee, Joshua", "position": "Forward"}
        ],
        
        "Newcastle United": [
            {"name": "Botman, Sven", "position": "Defender"},
            {"name": "Burn, Dan", "position": "Defender"},
            {"name": "Dubravka, Martin", "position": "Goalkeeper"},
            {"name": "Guimarães, Bruno", "position": "Midfielder"},
            {"name": "Hall, Lewis", "position": "Defender"},
            {"name": "Joelinton", "position": "Midfielder"},
            {"name": "Livramento, Tino", "position": "Defender"},
            {"name": "Longstaff, Sean", "position": "Midfielder"},
            {"name": "Pope, Nick", "position": "Goalkeeper"},
            {"name": "Schär, Fabian", "position": "Defender"},
            {"name": "Targett, Matt", "position": "Defender"},
            {"name": "Tonali, Sandro", "position": "Midfielder"},
            {"name": "Trippier, Kieran", "position": "Defender"},
            {"name": "Willock, Joe", "position": "Midfielder"},
            {"name": "Woltemade, Nick", "position": "Forward"}
        ],
        
        "Nottingham Forest": [
            {"name": "Anderson, Elliot", "position": "Midfielder"},
            {"name": "Awoniyi, Taiwo", "position": "Forward"},
            {"name": "Aurier, Serge", "position": "Defender"},
            {"name": "Biancone, Giulian", "position": "Defender"},
            {"name": "Dennis, Emmanuel", "position": "Forward"},
            {"name": "Felipe", "position": "Defender"},
            {"name": "Gibbs-White, Morgan", "position": "Midfielder"},
            {"name": "Hennessey, Wayne", "position": "Goalkeeper"},
            {"name": "Lingard, Jesse", "position": "Midfielder"},
            {"name": "McKenna, Scott", "position": "Defender"},
            {"name": "Niakhaté, Moussa", "position": "Defender"},
            {"name": "O'Brien, Lewis", "position": "Midfielder"},
            {"name": "Richards, Omar", "position": "Defender"},
            {"name": "Surridge, Sam", "position": "Forward"},
            {"name": "Toffolo, Harry", "position": "Defender"},
            {"name": "Turner, Matt", "position": "Goalkeeper"},
            {"name": "Williams, Neco", "position": "Defender"},
            {"name": "Wood, Chris", "position": "Forward"},
            {"name": "Worrall, Joe", "position": "Defender"},
            {"name": "Yates, Ryan", "position": "Midfielder"}
        ],
        
        "Sunderland": [
            {"name": "Abdul Samed, Salis", "position": "Midfielder"},
            {"name": "Bellingham, Jobe", "position": "Midfielder"},
            {"name": "Broadhead, Nathan", "position": "Forward"},
            {"name": "Dewsbury-Hall, Kiernan", "position": "Midfielder"},
            {"name": "Ekinde, Hugo Ekitike", "position": "Forward"},
            {"name": "Gomes, Claudio", "position": "Midfielder"},
            {"name": "Gooch, Lyndon", "position": "Midfielder"},
            {"name": "Hume, Trai", "position": "Defender"},
            {"name": "Mengi, Teden", "position": "Defender"},
            {"name": "Michut, Edouard", "position": "Midfielder"},
            {"name": "Neil, Dan", "position": "Midfielder"},
            {"name": "Patterson, Anthony", "position": "Goalkeeper"},
            {"name": "Prichard, Alex", "position": "Midfielder"},
            {"name": "Savage, Charlie", "position": "Midfielder"},
            {"name": "Stewart, Ross", "position": "Forward"},
            {"name": "Ugarte, Manuel", "position": "Midfielder"},
            {"name": "Wright, Bailey", "position": "Defender"}
        ],
        
        "Tottenham Hotspur": [
            {"name": "Bentancur, Rodrigo", "position": "Midfielder"},
            {"name": "Bissouma, Yves", "position": "Midfielder"},
            {"name": "Davies, Ben", "position": "Defender"},
            {"name": "Dier, Eric", "position": "Defender"},
            {"name": "Forster, Fraser", "position": "Goalkeeper"},
            {"name": "Hojbjerg, Pierre-Emile", "position": "Midfielder"},
            {"name": "Kane, Harry", "position": "Forward"},
            {"name": "Kulusevski, Dejan", "position": "Forward"},
            {"name": "Lloris, Hugo", "position": "Goalkeeper"},
            {"name": "Maddison, James", "position": "Midfielder"},
            {"name": "Porro, Pedro", "position": "Defender"},
            {"name": "Richarlison", "position": "Forward"},
            {"name": "Romero, Cristian", "position": "Defender"},
            {"name": "Sessegnon, Ryan", "position": "Defender"},
            {"name": "Skipp, Oliver", "position": "Midfielder"},
            {"name": "Son Heung-min", "position": "Forward"},
            {"name": "Udogie, Destiny", "position": "Defender"},
            {"name": "Van de Ven, Micky", "position": "Defender"},
            {"name": "Vicario, Guglielmo", "position": "Goalkeeper"}
        ],
        
        "West Ham United": [
            {"name": "Aguerd, Nayef", "position": "Defender"},
            {"name": "Areola, Alphonse", "position": "Goalkeeper"},
            {"name": "Bowen, Jarrod", "position": "Forward"},
            {"name": "Cornet, Maxwel", "position": "Forward"},
            {"name": "Coufal, Vladimír", "position": "Defender"},
            {"name": "Cresswell, Aaron", "position": "Defender"},
            {"name": "Downes, Flynn", "position": "Midfielder"},
            {"name": "Fabianski, Lukasz", "position": "Goalkeeper"},
            {"name": "Fornals, Pablo", "position": "Midfielder"},
            {"name": "Ings, Danny", "position": "Forward"},
            {"name": "Johnson, Ben", "position": "Defender"},
            {"name": "Kehrer, Thilo", "position": "Defender"},
            {"name": "Kudus Mohammed, Mohammed", "position": "Midfielder"},
            {"name": "Lanzini, Manuel", "position": "Midfielder"},
            {"name": "Ogbonna, Angelo", "position": "Defender"},
            {"name": "Paquetá, Lucas", "position": "Midfielder"},
            {"name": "Soucek, Tomás", "position": "Midfielder"},
            {"name": "Zouma, Kurt", "position": "Defender"}
        ],
        
        "Wolverhampton Wanderers": [
            {"name": "Ait-Nouri, Rayan", "position": "Defender"},
            {"name": "Bentley, Dan", "position": "Goalkeeper"},
            {"name": "Chiquinho", "position": "Forward"},
            {"name": "Collins, Nathan", "position": "Defender"},
            {"name": "Cunha, Matheus", "position": "Forward"},
            {"name": "Dawson, Craig", "position": "Defender"},
            {"name": "Gomes, Toti", "position": "Defender"},
            {"name": "Hwang Hee-chan", "position": "Forward"},
            {"name": "Jimenez, Raúl", "position": "Forward"},
            {"name": "Kalajdzic, Sasa", "position": "Forward"},
            {"name": "Kilman, Max", "position": "Defender"},
            {"name": "Lembikisa, Dexter", "position": "Defender"},
            {"name": "Lemina, Mario", "position": "Midfielder"},
            {"name": "Moutinho, João", "position": "Midfielder"},
            {"name": "Neto, Pedro", "position": "Forward"},
            {"name": "Otto, Jonny", "position": "Defender"},
            {"name": "Patrício, Rui", "position": "Goalkeeper"},
            {"name": "Sá, José", "position": "Goalkeeper"},
            {"name": "Semedo, Nélson", "position": "Defender"},
            {"name": "Traoré, Adama", "position": "Forward"},
            {"name": "Traoré, Boubacar", "position": "Midfielder"}
        ]
        }

            
        # formations = ["4-2-3-1", "4-4-2", "4-3-3", "4-3-2-1", "3-4-3", 
        #               "3-5-2", "5-3-2", "4-1-4-1", "4-4-1-1", "4-2-4"]
    def get_formation(positions):
        goalkeepers = positions.count("Goalkeeper")
        defenders = positions.count("Defender")
        midfielders = positions.count("Midfielder")
        forwards = positions.count("Forward")  # Changed from "Strikers" to "Forward"
        # Some players might be marked as "Striker" instead of "Forward"
        strikers = positions.count("Striker")
        
        total_strikers_forwards = forwards + strikers
        
        # Check common formations
        if goalkeepers == 1 and defenders == 4 and midfielders == 4 and total_strikers_forwards == 2:
            return '4-4-2'
        elif goalkeepers == 1 and defenders == 4 and midfielders == 3 and total_strikers_forwards == 3:
            return '4-3-3'
        elif goalkeepers == 1 and defenders == 3 and midfielders == 5 and total_strikers_forwards == 2:
            return '3-5-2'
        elif goalkeepers == 1 and defenders == 4 and midfielders == 2 and total_strikers_forwards == 3:
            return '4-2-3-1'
        elif goalkeepers == 1 and defenders == 5 and midfielders == 3 and total_strikers_forwards == 2:
            return '5-3-2'
        else:
            return None  # Return None instead of text_input

    # Main code
    team = st.selectbox(
        "Please select the home team from the Premier league", 
        list(team_players.keys()), 
        index=None, 
        placeholder="Please select the home team"
    )

    if team:
        players = team_players[team]
        player_names = [player['name'] for player in players]
        
        st.write(f'**Players for {team}**')
        
        # Use player_names for the multiselect, not team_players[team]
        selected_players = st.multiselect(
            'Select the 11 starting players', 
            player_names
        )
        
        if len(selected_players) != 11:
            st.error("Please select exactly 11 starting players")
        else:
            # Get the full player objects for selected players
            selected_player_objects = [player for player in players if player['name'] in selected_players]
            positions = [player['position'] for player in selected_player_objects]
            
            # Call the function
            formation = get_formation(positions)
            
            if formation:
                st.success(f'Selected formation: **{formation}**')
            else:
                # If no formation matches, ask user to input it
                formation = st.text_input(
                    "Could not determine formation automatically. Please enter the formation (e.g., 4-4-2):"
                )
                if formation:
                    st.success(f'Custom formation: **{formation}**')




if __name__ == '__main__':
    main()