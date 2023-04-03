```mermaid
classDiagram
    Peli -- "2..8" Pelaaja
    Peli -- "2" Noppa
    Peli -- "1" Pelilauta
    Pelilauta -- "40" Ruutu
    note for Ruutu "Tietää seuraavan ruudun"
    Pelaaja -- "1" Pelinappula
    Ruutu <|-- Pelinappula : sijaitsee
```
