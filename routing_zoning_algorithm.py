import pandas as pd
import numpy as np
from itertools import combinations, pairwise
import copy
import dijkstar


class RoutingZoningAlgorithm:
    def __init__(self) -> None:
        self.output = self.get_data()

    def get_data(self):
        # Import data

        demand_input = pd.DataFrame(pd.read_excel(r"C:\Users\Sava\Desktop\OPPPPython\Routing-Zoning Algorithm\Rutiranje_Zoniranje.xlsx", sheet_name="Rutiranje_Zoniranje_Potraznja"))

        distance_input = pd.DataFrame(pd.read_excel(r"C:\Users\Sava\Desktop\OPPPPython\Routing-Zoning Algorithm\Rutiranje_Zoniranje.xlsx", sheet_name="Rutiranje_Zoniranje_Matrica"))

        distance_input.pop("DistanceFROM/DistanceTO")

        # Functions

        def create_dict_with_list_values(input_list):
            """This function creates a dictionary with values that represent a list. 
            This is done to make it easier to find the min distance between the nodes."""
            dic = {}
            for s, t in enumerate(input_list):
                dic[s+1] = t
            return dic

        def nearest_neighbor(distance):
            """This function is used to find the shortest path between nodes using the nearest neighbor algorithm."""
            route = [depot]
            nearest_node = distance[depot].index(min(distance[depot])) + 1
            route.append(nearest_node)
            for length in range(1, len(distance) + 1):
                distance[length][depot - 1] = float("inf")
            for u in range(len(distance) - 2):
                nearest_node = distance[nearest_node].index(min(distance[nearest_node])) + 1
                route.append(nearest_node)
                for a in range(1, len(distance) + 1):
                    distance[a][nearest_node - 1] = float("inf")
            return route

        def new_route(route):
            """This function creates a new route from the route obtained by the nearest neighbor algorithm."""
            new_r = {}
            for length_route in range(len(route)):
                new_r[route[length_route]] = nearest_neighbor_route[length_route]
            return new_r

        def distance_between_list_nodes(c_i_j_list, demand_in_node):
            """This function calculates the distance between pairs of nodes on the route c_i_j_list, 
            taking into account the capacity of the vehicle, 
            for example. (0,1) gives a list [0,1,0] -> distances between 0,1 and 1,0"""
            distance_combinations = []
            if vehicle_capacity >= demand_in_node:
                for list_node in pairwise(c_i_j_list):
                    distance_combinations.append(distance_input[nearest_neighbor_new_route[list_node[0]]][nearest_neighbor_new_route[list_node[1]]-1])
                return sum(distance_combinations)
            else:
                return float("inf")

        # Input variables
        vehicle_capacity = 12
        depot = 1

        # Writing infinity on diagonal values instead of 0
        for j in range(len(distance_input.index)):
            for i in range(len(distance_input.index)):
                if distance_input.iat[i, j] == 0:
                    distance_input.iat[i, j] = float("inf")

        # Creating dictionary from demand in nodes
        demand_in_nodes = {}
        for demand in range(len(demand_input.index)):
            demand_in_nodes[int(demand_input.iloc[demand][0])] = demand_input.iloc[demand][1]
        demand_in_nodes[depot] = 0

        # Creating dictionary-ja from distance matrix for easy data calculation
        distance_input = distance_input.values.tolist()

        distance_input = create_dict_with_list_values(distance_input)
        distance_input2 = copy.deepcopy(distance_input)
        # Finding nearest neighbor
        nearest_neighbor_route = nearest_neighbor(distance_input2)

        # Creating a new route after finding the nearest neighbor
        nearest_neighbor_new_route = new_route(np.arange(len(nearest_neighbor_route)))  # kljuc izmedju route, moze i nearest_neighbor_new_route = np.arange(len(nearest_neighbor_route))

        # Creating new routes from pairs of nodes 1x2 e.g. (0,1) ->[0,1,0] (0,2) -> [0,1,2,0]
        movement_route = {}
        for node in list(combinations(nearest_neighbor_new_route, 2)):
            movement_route[node] = np.arange(int(node[0]), int(node[1])+1)
            movement_route[node] = np.append(movement_route[node], 0)
            movement_route[node][0] = 0

        # The total demand along the route that is allowed/not allowed
        demand_along_route = {}
        for nodes_i_j in movement_route:
            route_demand = []
            for node in movement_route[nodes_i_j]:
                demand = demand_in_nodes[nearest_neighbor_new_route[node]]
                route_demand.append(demand)
                demand_along_route[nodes_i_j] = sum(route_demand)

        # Total distance along the new route that is admissible (if it is not admissible, the distance is infinite)
        c_i_j = {}
        for nodes_i_j in movement_route:
            c_i_j[nodes_i_j] = distance_between_list_nodes(movement_route[nodes_i_j], demand_along_route[nodes_i_j])
            if c_i_j[nodes_i_j] == float("inf"):
                c_i_j.pop(nodes_i_j)

        # Finding shortest_path using Dijkstra's algorithm.
        graph = dijkstar.Graph()
        for dijkstra in c_i_j:
            graph.add_edge(dijkstra[0], dijkstra[1], c_i_j[dijkstra])
        shortest_path = dijkstar.find_path(graph, 0, len(nearest_neighbor_new_route)-1)
        shortest_path_dijkstra = shortest_path.nodes

        # Finding vehicle movement paths
        vehicle_movement_paths = []
        for new_route in pairwise(shortest_path_dijkstra):
            vehicle_movement_paths.append(movement_route[new_route])

        # Returning old node names in new routes
        vehicle_movement_paths_final = []
        for route_final in vehicle_movement_paths:
            input_vehicle_movement_paths_final = []
            for node_final in route_final:
                input_vehicle_movement_paths_final.append(nearest_neighbor_new_route[node_final])
            vehicle_movement_paths_final.append(input_vehicle_movement_paths_final)
        return vehicle_movement_paths_final
