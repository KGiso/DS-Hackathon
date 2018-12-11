
from package_read_file.read_file import *
from package_clustering.random_centroid import random_centroid
from package_clustering.cost_func import cost_func
from package_clustering.re_assignment import re_assignment
from package_clustering.package_lloyd.k_means import k_means
from package_fraud.fraud_detector import *

import sys
import time
import numpy as np

def main(argv):

	'''1. pre-defined parameters'''
	dataset = str(sys.argv[1])
	# epsilon = float(sys.argv[2])
	experiment_round = 1
	k = int(sys.argv[2]) # number of centroids

	method_num = 1
	decimal_place = 5
	given_iterations = 3 # given iteration for Blum-dp


	'''2. read input'''
	if dataset in ["hackathon"]:
		node_list = build_from_csv(dataset, decimal_place)
	else:
		print("*-" * 20)
		print("Input dataset options: hackathon")
		print("Try next time. See you then.")
		print("*-" * 20)
		sys.exit()

	# # test
	# print("I read these:")
	# for i in range(200):
	# 	print(node_list[i].features, node_list[i].cluster)
	# print(len(node_list))



	# fraud detection
	data_list = fast_transaction(node_list)
	# data_list = copy.deepcopy(over_limit_transaction(data_list))

	# test
	print("I read these:")
	for i in range(200):
		print(data_list[i].fraud, node_list[i].cluster)
	sys.exit()
	
	'''3. evaluations'''
	cost = np.zeros((method_num, experiment_round))
	final_cost = [0.0] * method_num
	best_final_cost = [0.0] * method_num
	
	for i in range(experiment_round):
		# generate the k initial centroids for all methods
		initial_centroid_list = random_centroid(node_list, k)

		# *************************************************************

		# 0. k-means
		# start = time.time()

		tuple_k_means = k_means(node_list, initial_centroid_list, k, decimal_place)

		# end = time.time()
		
		# calculate the value for final illustration
		final_centroid_list = tuple_k_means[0]
		# iterations[0] = iterations[0] + tuple_k_means[1]
		
		final_data_list = re_assignment(node_list, final_centroid_list, k, decimal_place)
		# cost[0] = cost[0] + cost_func(final_data_list, final_centroid_list, k, decimal_place)
		cost[0][i] = cost_func(final_data_list, final_centroid_list, k, decimal_place)

		# # test
		# print("round:", i)
		# print("0:", cost[0][i] / cost[0][i])

		# run_time[0] = run_time[0] + end - start

		# # test
		# print("+_+_" * 10)
		# print("final centroids lloyd:")
		# for j in range(len(final_centroid_list)):
		# 	print(final_centroid_list[j].features)
		# print("final data list:")
		# cluster_list = [x.cluster for x in final_data_list]
		# print(cluster_list)

		# *************************************************************

		# # 1. my algorithm
		# start = time.time()

		# # let my algorithm run until it converges
		# tuple_lu = k_means_lu(node_list, initial_centroid_list, k, decimal_place, epsilon, tuple_k_means[1])

		# end = time.time()
		
		# # calculate the value for final illustration
		# final_centroid_list_lu = tuple_lu[0]
		# iterations[1] = iterations[1] + tuple_lu[1]

		# final_data_list_lu = re_assignment(node_list, final_centroid_list_lu, k, decimal_place)
		# # cost[1] = cost[1] + cost_func(final_data_list_lu, final_centroid_list_lu, k, decimal_place)
		# cost[1][i] = cost_func(final_data_list_lu, final_centroid_list_lu, k, decimal_place)

		# # # test
		# # print("1:", cost[1][i] / cost[0][i])

		# run_time[1] = run_time[1] + end - start

		# # compute the overall privacy budget
		# # every two iterations, my algorithm applies DP once
		# epsilon_overall = np.around(epsilon * tuple_lu[1] / 2 + epsilon, decimal_place)
		# priv_budget = priv_budget + epsilon_overall

		# # # test
		# # print("+_+_" * 10)
		# # print("final dp centroid lu:")
		# # for j in range(len(final_centroid_list_lu)):
		# # 	print(final_centroid_list_lu[j].features)
		# # print("final data list:")
		# # cluster_list_lu = [x.cluster for x in final_data_list_lu]
		# # print(cluster_list_lu)
		
		# # **************************************************************

		# # 2. Su-dp
		# start = time.time()

		# # run it in opt_iterations
		# rho = 0.225
		# epsilon_in_iteration = np.around(np.sqrt(500 * (k ** 3) / (len(node_list) ** 2) * ((len(node_list[0].features) + np.cbrt(4 * len(node_list[0].features) * (rho ** 2))) ** 3)), decimal_place)
		# if epsilon_in_iteration > epsilon_overall:
		# 	opt_iterations = 1
		# 	epsilon_in_iteration = epsilon_overall
		# else:
		# 	opt_iterations = np.ceil(epsilon_overall / epsilon_in_iteration)

		# tuple_su = k_means_su(node_list, initial_centroid_list, k, decimal_place, epsilon_in_iteration, opt_iterations)

		# end = time.time()
		
		# # calculate the value for final illustration
		# final_centroid_list_su = tuple_su[0]
		# iterations[2] = iterations[2] + tuple_su[1]

		# final_data_list_su = re_assignment(node_list, final_centroid_list_su, k, decimal_place)
		# # cost[2] = cost[2] + cost_func(final_data_list_su, final_centroid_list_su, k, decimal_place)
		# cost[2][i] = cost_func(final_data_list_su, final_centroid_list_su, k, decimal_place)

		# # # test
		# # print("2:", cost[2][i] / cost[0][i])

		# run_time[2] = run_time[2] + end - start

		# # # test
		# # print("+_+_" * 10)
		# # print("final dp centroid su:")
		# # for j in range(len(final_centroid_list_su)):
		# # 	print(final_centroid_list_su[j].features)
		# # print("final data list:")
		# # cluster_list_su = [x.cluster for x in final_data_list_su]
		# # print(cluster_list_su)

		# # **************************************************************

		# # 3. PrivGene
		# start = time.time()

		# # assign and compute key arguments as suggested by the referenced paper
		# m = 200
		# m_p = 10
		# x = 1.25 * (10 * (-3))
		# iteration = int(max(8, np.around(x * len(node_list) * epsilon_overall / m_p)))
		# epsilon_in_iteration = np.around(epsilon_overall / iteration, decimal_place)

		# tuple_privgene = k_means_privgene(node_list, k, m, m_p, decimal_place, epsilon_in_iteration, iteration)

		# end = time.time()
		
		# # calculate the value for final illustration
		# final_centroid_list_privgene = tuple_privgene[0]
		# iterations[3] = iterations[3] + tuple_privgene[1]

		# final_data_list_privgene = re_assignment(node_list, final_centroid_list_privgene, k, decimal_place)
		# # cost[3] = cost[3] + cost_func(final_data_list_privgene, final_centroid_list_privgene, k, decimal_place)
		# cost[3][i] = cost_func(final_data_list_privgene, final_centroid_list_privgene, k, decimal_place)

		# # # test
		# # print("3:", cost[3][i] / cost[0][i])

		# run_time[3] = run_time[3] + end - start

		# # # test
		# # print("+_+_" * 10)
		# # print("final dp centroid privgene:")
		# # for j in range(len(final_centroid_list_privgene)):
		# # 	print(final_centroid_list_privgene[j].features)
		# # print("final data list:")
		# # cluster_list_privgene = [x.cluster for x in final_data_list_privgene]
		# # print(cluster_list_privgene)

		# # **************************************************************

		# # 4. Blum-dp
		# start = time.time()

		# epsilon_in_iteration = np.around(epsilon_overall / given_iterations, decimal_place)

		# tuple_blum = k_means_blum(node_list, initial_centroid_list, k, decimal_place, epsilon_in_iteration, given_iterations)

		# end = time.time()
		
		# # calculate the value for final illustration
		# final_centroid_list_blum = tuple_blum[0]
		# iterations[4] = iterations[4] + tuple_blum[1]

		# final_data_list_blum = re_assignment(node_list, final_centroid_list_blum, k, decimal_place)
		# # cost[4] = cost[4] + cost_func(final_data_list_blum, final_centroid_list_blum, k, decimal_place)
		# cost[4][i] = cost_func(final_data_list_blum, final_centroid_list_blum, k, decimal_place)

		# # # test
		# # print("4:", cost[4][i] / cost[0][i])

		# run_time[4] = run_time[4] + end - start

		# # # test
		# # print("+_+_" * 10)
		# # print("final dp centroid blum:")
		# # for j in range(len(final_centroid_list_blum)):
		# # 	print(final_centroid_list_blum[j].features)
		# # print("final data list:")
		# # cluster_list_blum = [x.cluster for x in final_data_list_blum]
		# # print(cluster_list_blum)

		# # **************************************************************

		# # 5. Dwork-dp
		# start = time.time()

		# tuple_dwork = k_means_dwork(node_list, initial_centroid_list, k, decimal_place, epsilon_overall)

		# end = time.time()

		# # calculate the value for final illustration
		# final_centroid_list_dwork = tuple_dwork[0]
		# iterations[5] = iterations[5] + tuple_dwork[1]

		# final_data_list_dwork = re_assignment(node_list, final_centroid_list_dwork, k, decimal_place)
		# # cost[5] = cost[5] + cost_func(final_data_list_dwork, final_centroid_list_dwork, k, decimal_place)
		# cost[5][i] = cost_func(final_data_list_dwork, final_centroid_list_dwork, k, decimal_place)

		# # # test
		# # print("5:", cost[5][i] / cost[0][i])

		# run_time[5] = run_time[5] + end - start

		# # # test
		# # print("+_+_" * 10)
		# # print("final dp centroid dwork:")
		# # for j in range(len(final_centroid_list_dwork)):
		# # 	print(final_centroid_list_dwork[j].features)
		# # print("final data list:")
		# # cluster_list_dwork = [x.cluster for x in final_data_list_dwork]
		# # print(cluster_list_dwork)

		# # **************************************************************

		# # 6. GUPT
		# start = time.time()

		# # suggested partition numbers by the GUPT paper
		# partition_num = int(np.ceil(len(node_list) ** (0.4)))

		# # GUPT doesn't need a set of initial centroids
		# tuple_gupt = k_means_gupt(node_list, k, decimal_place, epsilon, partition_num)

		# end = time.time()

		# # calculate the value for final illustration
		# final_centroid_list_gupt = tuple_gupt[0]
		# iterations[6] = iterations[6] + tuple_gupt[1]

		# final_data_list_gupt = re_assignment(node_list, final_centroid_list_gupt, k, decimal_place)
		# # cost[6] = cost[6] + cost_func(final_data_list_gupt, final_centroid_list_gupt, k, decimal_place)
		# cost[6][i] = cost_func(final_data_list_gupt, final_centroid_list_gupt, k, decimal_place)

		# # # test
		# # print("6:", cost[6][i] / cost[0][i])

		# run_time[6] = run_time[6] + end - start

		# # calculate the overall epsilon for GUPT
		# priv_budget_gupt = np.around(epsilon * tuple_gupt[1], decimal_place) + priv_budget_gupt

		# # # test
		# # print("+_+_" * 10)
		# # print("final dp centroid gupt:")
		# # for j in range(len(final_centroid_list_gupt)):
		# # 	print(final_centroid_list_gupt[j].features)
		# # print("final data list:")
		# # cluster_list_gupt = [x.cluster for x in final_data_list_gupt]
		# # print(cluster_list_gupt)


	'''4. display results'''
	print("*" * 60)
	# pre-defined parameters
	print("Dataset:", sys.argv[1], "->", len(node_list), "*", len(node_list[0].features))
	print("Decimal place:", decimal_place)
	print("Number of clusters:", k)
	print("experiment rounds:", experiment_round)
	print("-" * 60)

	

	

	# final cost == illustrated results
	print("FINAL COST:")
	for i in range(method_num):
		print("Lloyd:")
		print("unsorted:")
		print(cost[i])
		cost[i].sort()
		print("sorted:")
		print(cost[i])
	print("*" * 60)


# main entry
if __name__ == "__main__":
	main(sys.argv)
else:
	print("main.py is the starter!\nUse command: python3 main.py to run it.")
