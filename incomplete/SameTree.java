// WIP, still wrong - fix the cases

import java.util.*;

public class SameTree {
    static Queue<TreeNode> queueP;
    static Queue<TreeNode> queueQ;

    public static boolean isSameTree(TreeNode p, TreeNode q) {
        queueP = new LinkedList<>();
        queueQ = new LinkedList<>();

        queueP.add(p);
        queueQ.add(q);

        boolean isUnequal = false;

        boolean queuePempty = queueP.isEmpty();
        boolean queueQempty = queueQ.isEmpty();
        boolean bothHaveNodes = !queuePempty && !queueQempty;
        
        while(bothHaveNodes) { // while they both have nodes
            TreeNode currP = queueP.poll();
            TreeNode currQ = queueQ.poll();

            if((currP == null) && (currQ == null)) {

            }

            if(((currP == null) && (currQ != null)) || (currP != null) && (currQ == null)) {
                isUnequal = true;
                break;
            }

            if(currP.val != currQ.val) {
                isUnequal = true;
                break;
            }

            pBFS(currP);
            qBFS(currQ);
        }

        if(isUnequal) {
            return false;
        } else if((queuePempty && !queueQempty) || queueQempty && !queuePempty) {
            return false;
        } else {
            return true;
        }
    }

    public static void pBFS(TreeNode treenode) {
        if(treenode.left == null && treenode.right == null) { // current treenode is a leaf, don't add more
        
        } else {
            queueP.add(treenode.left);
            queueP.add(treenode.right);
        }   
    }

    public static void qBFS(TreeNode treenode) {
        if(treenode.left == null && treenode.right == null) {
        
        } else {
            queueQ.add(treenode.left);
            queueQ.add(treenode.right);
        } 
    }
}

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}
