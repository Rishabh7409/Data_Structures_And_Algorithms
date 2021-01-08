

public class Graph_Floyd_Warshall_Algorithm {

    int total_vertices;
    int [][]graph;

    Graph_Floyd_Warshall_Algorithm(int number_of_vertices){
        graph=new int[number_of_vertices][number_of_vertices];
        this.total_vertices=number_of_vertices;
    }

    private void Add_Edge(int src,int dest,int weight){
        graph[src][dest]=weight;
    }

    private void Floyd_Warshall(){
        //Create Input Matrix From Given Graph
//        long max_val=100000;
        long [][]input=new long[this.total_vertices][this.total_vertices];
        for(int i=0;i<this.graph.length;i++){
            for(int j=0;j<this.graph.length;j++){
                if(i==j){
                    input[i][j]=0;
                }
                else if(this.graph[i][j]==0){
                    input[i][j]=Integer.MAX_VALUE;
                }
                else {
                    input[i][j]=this.graph[i][j];
                }
            }
        }

        for(int x=0;x<this.total_vertices;x++){
            for(int y=0;y<this.total_vertices;y++){
                for(int z=0;z<this.total_vertices;z++){
                    input[y][z]=Math.min(input[y][x]+input[x][z],input[y][z]);
                }
            }
        }
        Display_Shortest_Path(input);
    }

    private void Display_Shortest_Path(long [][]output){
        System.out.println("The Shortest Path Between All The Edges Are");
        for(long []ar:output){
            for(long ele:ar){
                if(ele!=Integer.MAX_VALUE){
                    System.out.print(ele+" ");
                }
                else {
                    System.out.print("N ");
                }
            }
            System.out.println();
        }
    }

    private void Display_Graph(){
        for(int []ar:this.graph){
            for(int ele:ar){
                System.out.print(ele+" ");
            }
            System.out.println();
        }
    }

    public static void main(String []args){
        Graph_Floyd_Warshall_Algorithm floyd=new Graph_Floyd_Warshall_Algorithm(4);
        floyd.Add_Edge(0,1,3);
        floyd.Add_Edge(0,3,7);
        floyd.Add_Edge(1,2,2);
        floyd.Add_Edge(1,0,8);
        floyd.Add_Edge(2,3,1);
        floyd.Add_Edge(2,0,5);
        floyd.Add_Edge(3,0,2);

        floyd.Display_Graph();
        floyd.Floyd_Warshall();
    }


}
