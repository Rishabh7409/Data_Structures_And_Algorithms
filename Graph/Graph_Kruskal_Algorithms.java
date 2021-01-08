//Steps For Performing Kruskal Algorithm

//1. Sort all the edges in non-decreasing order of their weight.
//2. Pick the smallest edge. Check if it forms a cycle with the spanning tree formed so far. If cycle is not formed, include this edge. Else, discard it.
//3. Repeat step#2 until there are (V-1) edges in the spanning tree.


import java.util.*;

public class Graph_Kruskal_Algorithms {

    static class Sort_By_Weight implements Comparator<Graph_Edge>{
        public int compare(Graph_Edge g1,Graph_Edge g2){
            return g1.weight-g2.weight;
        }
    }

    private Graph_Edge []edges;
    int number_of_edges=0;
    int number_of_Vertices;
    Graph_Kruskal_Algorithms(int vertices_n,int edges_n){
        this.edges=new Graph_Edge[edges_n];  //Stores All The Edges Of Graph
        this.number_of_Vertices=vertices_n;
    }

    private void Add_Edge(int src,int dest,int weight){
        edges[this.number_of_edges++]=new Graph_Edge(src,dest,weight);
    }

    // private void Display_Graph(){
    //     for(Graph_Edge ed:this.edges){
    //         System.out.println(ed.source+" "+ed.destination+" "+ed.weight);
    //     }
    // }

    private int Find_Parent(int []Parent,int val){
        //Finding Absolute Parent Of A Node
        if(Parent[val]==val){
            return val;
        }
        return Find_Parent(Parent,Parent[val]);
    }

    private void Kruskal_Algorithm_For_Minimal_Spanning_Tree(){
        //Sort The Edges Acc To Weight
        Arrays.sort(this.edges,new Sort_By_Weight());

        int []Parent=new int[this.number_of_edges]; //For Storing Parent Of Vertices
        for (int i=0;i<this.number_of_edges;i++){
            Parent[i]=i;        //Initially The Nodes Parent Will Be Themselves Only
        }
        Graph_Edge []output=new Graph_Edge[this.number_of_Vertices-1];  //Spanning Tree Will Be Having Vertices-1 Edges
        int count=0,x=0;
        while (count!=this.number_of_Vertices-1){ //while edges added not equal to vertices-1
            Graph_Edge curr_edge=this.edges[x];
            int source_parent=Find_Parent(Parent,curr_edge.source);
            int dest_parent=Find_Parent(Parent,curr_edge.destination);
            //if source_p and dest_p does not have same root parent therefore adding them will not form a cycle
            if(source_parent!=dest_parent){
                output[count]=curr_edge;
                count++;
                Parent[source_parent]=dest_parent;  //Union Operation
            }
            x++;
        }
        System.out.println("The Minimal Spanning Tree Is: ");
        // Join All the output vertices to get minimum spanning tree
        for(Graph_Edge ed:output){
            System.out.println("Source : "+ed.source+"   Destination : "+ed.destination+"   Distance : "+ed.weight);
        }
    }

    public static void main(String []args){
        int total_vertices=9;
        int total_edges=14;
        Graph_Kruskal_Algorithms kruskal=new Graph_Kruskal_Algorithms(total_vertices,total_edges);

        kruskal.Add_Edge(0,1,4);
        kruskal.Add_Edge(0,7,8);
        kruskal.Add_Edge(1,7,11);
        kruskal.Add_Edge(1,2,8);
        kruskal.Add_Edge(2,3,7);
        kruskal.Add_Edge(2,8,2);
        kruskal.Add_Edge(2,5,4);
        kruskal.Add_Edge(3,4,9);
        kruskal.Add_Edge(3,5,14);
        kruskal.Add_Edge(4,5,10);
        kruskal.Add_Edge(5,6,2);
        kruskal.Add_Edge(6,8,6);
        kruskal.Add_Edge(6,7,1);
        kruskal.Add_Edge(7,8,7);


        kruskal.Kruskal_Algorithm_For_Minimal_Spanning_Tree();
    }

}
