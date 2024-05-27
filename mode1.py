from landsites import Land
from data_structures.bst import BinarySearchTree
from data_structures.bst import BSTInOrderIterator

class Mode1Navigator:
    """
    Student-TODO: short paragraph as per
    https://edstem.org/au/courses/14293/lessons/46720/slides/318306
    """

    def __init__(self, sites: list[Land], adventurers: int) -> None:
        """
        Initializes the object with a list of land sites and the number of adventurers.

        Complexity:
        Best-case and Worst-case : O(1)
        
        Explanation: 
        Reassignment of data are all done in constant operation. Therefore all operations have complexity of O(1)
        """
        self.adventurers = adventurers
        self.sites = sites
        

    def select_sites(self) -> list[tuple[Land, int]]:
        """
        This method selects land sites based on the number of adventurers available and the ratio of guardians to gold. 
        It iterates over the available land sites, calculates their ratio of guardians to gold, and adds them to a binary search tree (BST) based on this ratio. 
        Then, it traverses the BST in-order to select land sites in ascending order of their ratio. 
        For each land site, it assigns adventurers to the site until either all adventurers are assigned or there are no more guardians on the site. 
        It returns a list of tuples where each tuple contains a selected Land object and the number of adventurers assigned to it.
        
        Complexity:
        - Best-case: O(n) where n is the number of land sites.
        - Worst-case: O(n) where n is the number of land sites.
        
        Explanation:
        This method iterates over the available land sites once to calculate their ratio of guardians to gold, which has a time complexity of O(n). 
        Then, it adds the land sites to a binary search tree (BST) based on this ratio, which has a time complexity of O(n) for each insertion operation, 
        resulting in a total time complexity of O(n) for constructing the BST. 
        After constructing the BST, it traverses it in-order to select land sites, which has a time complexity of O(n). 
        Therefore, the overall time complexity of the method is O(n).

        """
        bst  = BinarySearchTree()
        num_adventurer = self.adventurers
        list = []

        for land in self.sites:
            bst[land.get_guardians() / land.get_gold()] = land

        in_order = [node.item for node in BSTInOrderIterator(bst.root)]

        for land in in_order:
            if num_adventurer >= land.get_guardians():
                selected = land.get_guardians()
                num_adventurer -= selected
            
            else:
                selected = num_adventurer
                num_adventurer = 0
            list.append((land, selected))
            
            if selected == 0:
                break
        return list




    def select_sites_from_adventure_numbers(self, adventure_numbers: list[int]) -> list[float]:
        """
        This method selects land sites and calculates the total rewards earned based on different numbers of adventurers for each scenario specified in the adventure_numbers list. 
        For each scenario, it first sets the number of adventurers according to the current scenario. 
        Then, it calls the select_sites method to select land sites based on the available number of adventurers. 
        After selecting land sites, it calculates the reward for each land site based on the ratio of adventurers to gold. 
        It then adds up the rewards for all selected land sites to calculate the total reward earned for the current scenario. 
        Finally, it adds the total reward earned for each scenario to a list and returns the list of total rewards.

        Complexity:
        - Best-case: O(A x N) where n is the number of scenarios (length of adventure_numbers) and N is the average number of land sites selected for each scenario.
        - Worst-case: O(A x N) where n is the number of scenarios (length of adventure_numbers) and N is the average number of land sites selected for each scenario.
        
        Explanation:
        This method iterates over each scenario specified in the adventure_numbers list, resulting in a time complexity of O(n), where n is the number of scenarios. 
        For each scenario, it calls the select_sites method, which has a time complexity of O(A) where A is the average number of land sites selected for each scenario. 
        Within the select_sites method, it iterates over the selected land sites and calculates the reward for each site, resulting in a time complexity of O(A). 
        Therefore, the total time complexity for processing all scenarios is O(A x N).
        """
    
        list = []
        for number in adventure_numbers:

            self.adventurers = number
            adventurer_list = self.select_sites()

            award = 0
            for land, adventurer in adventurer_list:
                reward = adventurer * land.get_gold() / land.get_guardians()
                award += min(reward, land.get_gold())
            
            list.append(award)
        
        return list

        
    def update_site(self, land: Land, new_reward: float, new_guardians: int) -> None:
        """
        This method updates the reward and number of guardians for a specified land site. 
        It takes a Land object representing the land site to be updated, along with the new reward value and the new number of guardians. 
        It then calls the set_gold method of the Land object to update the reward and the set_guardians method to update the number of guardians.

        Complexity:
        Best-case and Worst-case: O(1)
        
        Explanation:
        This method directly updates the reward and number of guardians for the specified land site by calling the set_gold and set_guardians methods, 
        each of which has a constant time complexity of O(1). Therefore, the overall time complexity of the method is O(1).
        """
        land.set_gold(new_reward)
        land.set_guardians(new_guardians)
