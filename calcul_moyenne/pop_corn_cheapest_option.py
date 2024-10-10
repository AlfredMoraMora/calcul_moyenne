def scenario_autobus():
    # Coût des billets
    price_per_ticket = 12
    total_tickets = 2
    total_ticket_price = price_per_ticket * total_tickets  # Total before discount
    tax_rate = 0.15

    # Économie en achetant les billets par paire
    discount = 2
    total_with_tax = total_ticket_price * (1 + tax_rate)
    total_with_discount = total_with_tax - discount

    # Coût d'autobus aujourd'hui
    bus_ticket_cost = 2.50

    # Coût total pour acheter les billets aujourd'hui
    total_cost = total_with_discount + bus_ticket_cost

    return total_cost


def scenario_uber():
    # Coût des billets
    price_per_ticket = 12
    total_tickets = 2
    total_ticket_price = price_per_ticket * total_tickets
    tax_rate = 0.15

    # Coût total des billets avec taxe (sans réduction)
    total_with_tax = total_ticket_price * (1 + tax_rate)

    # Coût de l'Über
    distance_km = 12
    base_uber_rate_per_km = 1  # Disons que c'est 1 $/km
    peak_surcharge_per_km = 0.25
    uber_rate_per_km = base_uber_rate_per_km + peak_surcharge_per_km

    uber_cost = distance_km * uber_rate_per_km  # Coût de l'aller-retour en Über

    # Coût total pour acheter les billets jeudi avec Über
    total_cost = total_with_tax + uber_cost

    return total_cost


def can_nicolas_buy_popcorn(best_cost):
    # Le coût d'un popcorn est de 5 $
    popcorn_price = 5
    budget = 30  # On suppose que Nicolas a un budget de 30 $

    if best_cost + popcorn_price <= budget:
        return True
    return False


def main():
    # Calcul du coût pour chaque scénario
    cost_autobus = scenario_autobus()
    cost_uber = scenario_uber()

    # Comparer les coûts
    if cost_autobus < cost_uber:
        best_option = "Prendre l'autobus aujourd'hui"
        best_cost = cost_autobus
    else:
        best_option = "Prendre l'Über jeudi"
        best_cost = cost_uber

    # Afficher la meilleure option
    print(f"La meilleure option est: {best_option}, avec un coût total de {best_cost:.2f} $")

    # Vérifier si Nicolas peut acheter un popcorn
    if can_nicolas_buy_popcorn(best_cost):
        print("Nicolas peut acheter un popcorn !")
    else:
        print("Nicolas ne peut pas acheter un popcorn.")


# Exécuter le programme
if __name__ == '__main__':
    main()