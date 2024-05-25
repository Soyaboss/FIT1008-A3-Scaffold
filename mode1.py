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
        Student-TODO: Best/Worst Case
        """
        self.adventurers = adventurers
        self.sites = sites
        

    def select_sites(self) -> list[tuple[Land, int]]:
        """
        Student-TODO: Best/Worst Case
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
        Student-TODO: Best/Worst Case
        """
        
    def update_site(self, land: Land, new_reward: float, new_guardians: int) -> None:
        """
        Student-TODO: Best/Worst Case
        """
        land.set_gold(new_reward)
        land.set_guardians(new_guardians)
