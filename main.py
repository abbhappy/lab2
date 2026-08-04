from model.track import Track
from model.genre import Genre


def main():
    print("=" * 60)
    print("The Domain Model")
    print("=" * 60)

    # ==========================================
    # Domain Model Classes Track and Genre:
    # ==========================================

    # 1. Create some tracks
    print("\nDomain Model Classes Track and Genre:")
    print("\nTRACKS CREATED")

    track1 = Track("T001", "Particule", "Miki", year=2025)
    track2 = Track("T002", "Lo Que Le Pasó a Hawaii", "Bad Bunny", year=2025)
    track3 = Track("T003", "Latinoamérica", "Calle 13", year=2010)
    track4 = Track("T004", "Aloha Aina Meds", "Ikaakamai", year=2021)
    track5 = Track("T005", "Le bruit et l'odeur", "Zebbda", year=1995)

    # Print tracks
    print(f"- {track1.title} by {track1.artist} ({track1.year}) [ ]")
    print(f"- {track2.title} by {track2.artist} ({track2.year}) [ ]")
    print(f"- {track3.title} by {track3.artist} ({track3.year}) [ ]")
    print(f"- {track4.title} by {track4.artist} ({track4.year}) [ ]")
    print(f"- {track5.title} by {track5.artist} ({track5.year}) [ ]")

    # 2. Create two genres
    print("\nGENRES CREATED")
    french_pop = Genre("G001", "French Pop")
    folk_protest = Genre("G002", "folk-infused protest song")

    print(f"- {french_pop.name} ({french_pop.track_count()} track(s))")
    print(f"  {folk_protest.name} ({folk_protest.track_count()} track(s))")

    # 3. Add tracks to their corresponding genre
    print("\n---")
    print("\n GENRES WITH ASSOCIATED TRACKS")

    # French Pop: track1 and track5
    french_pop.add_track(track1)   # Particule
    french_pop.add_track(track5)   # Le bruit et l'odeur

    # folk-infused protest song: track2, track3, track4, track5
    folk_protest.add_track(track2)  # Lo Que Le Pasó a Hawaii
    folk_protest.add_track(track3)  # Latinoamérica
    folk_protest.add_track(track4)  # Aloha Aina Meds
    folk_protest.add_track(track5)  # Le bruit et l'odeur

    # Print genres with their tracks
    print(f"\n- {french_pop.name} ({french_pop.track_count()} track(s)):")
    for track in french_pop.tracks:
        print(f"  - {track.title} by {track.artist}")

    print(f"\n- {folk_protest.name} ({folk_protest.track_count()} track(s)):")
    for track in folk_protest.tracks:
        print(f"  - {track.title} by {track.artist}")

    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()