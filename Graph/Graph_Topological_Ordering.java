

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Graph_Topological_Ordering {

    HashMap<Integer, ArrayList<Graph_Edge>> graph = new HashMap<>();
    ArrayList<Character> vertices;

    Graph_Topological_Ordering(ArrayList<Character> arr) {
        this.vertices = arr;
    }

    private void add_Directed_Edge(int src, int dest, int weight) {
        Graph_Edge edge = new Graph_Edge(src, dest, weight);
        ArrayList<Graph_Edge> ar;
        if (this.graph.containsKey(src)) {
            this.graph.get(src).add(edge);

        } else {
            ar = new ArrayList<>();
            ar.add(edge);
            this.graph.put(src, ar);
        }
        if (!this.graph.containsKey(dest)) {
            this.graph.put(dest, new ArrayList<>());
        }
    }

    private void Adjacency_List() {
        for (Map.Entry<Integer, ArrayList<Graph_Edge>> itr : this.graph.entrySet()) {
            System.out.print(this.vertices.get(itr.getKey()) + " : ");
            for (Graph_Edge ed : itr.getValue()) {
                System.out.print(this.vertices.get(ed.destination) + " ");
            }
            System.out.println();
        }
    }

    void DFS_Traversal() {
        HashMap<Integer, Boolean> visited = new HashMap<>();
        for (Map.Entry<Integer, ArrayList<Graph_Edge>> it : this.graph.entrySet()) {
            visited.put(it.getKey(), false);
        }
        ArrayList<Character> dfs = new ArrayList<>();
        for (Map.Entry<Integer, ArrayList<Graph_Edge>> itr : this.graph.entrySet()) {
            if (!visited.get(itr.getKey())) {
                DFS_Helper(dfs, visited, itr.getKey());
            }
        }
        System.out.println(dfs);
    }

    void DFS_Helper(ArrayList<Character> dfs, HashMap<Integer, Boolean> visited, int key) {
        visited.put(key, true);
        for (Graph_Edge ed : this.graph.get(key)) {
            if (!visited.get(ed.destination)) {
                DFS_Helper(dfs, visited, ed.destination);
            }
        }
        dfs.add(0,this.vertices.get(key));
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        ArrayList<Character> chr = new ArrayList<>();
        for (int i = 0; i < 6; i++) {
            chr.add(scan.next().charAt(0));
        }
        scan.close();
        Graph_Topological_Ordering gdp = new Graph_Topological_Ordering(chr);

        gdp.add_Directed_Edge(2,1,0);
        gdp.add_Directed_Edge(3,2,0);
        gdp.add_Directed_Edge(3,0,0);
        gdp.add_Directed_Edge(4,1,0);
        gdp.add_Directed_Edge(4,0,0);
        gdp.add_Directed_Edge(0,5,0);
        gdp.add_Directed_Edge(5,3,0);
        gdp.Adjacency_List();
        gdp.DFS_Traversal();

    }
}
