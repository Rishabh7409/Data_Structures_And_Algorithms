//GeeksforGeeks

//An Island Is A Connected group of 1's

//A Single 1 is also An Island



public class Graph_Number_Of_Islands {

    private void DFS(boolean [][]visited,int [][]matrix,int row,int col,int n){

        if(row<0 || col<0 || row>=n || col>=matrix[0].length ||visited[row][col]||matrix[row][col]==0){
            //If The Current Block Is Not Safe
            return;
        }
        visited[row][col]=true;
        //Recursive Call For All The Neighbouring Cells
        DFS(visited,matrix,row-1,col-1,n);
        DFS(visited,matrix,row-1,col+1,n);
        DFS(visited,matrix,row-1,col,n);
        DFS(visited,matrix,row+1,col-1,n);
        DFS(visited,matrix,row+1,col+1,n);
        DFS(visited,matrix,row+1,col,n);
        DFS(visited,matrix,row,col-1,n);
        DFS(visited,matrix,row,col+1,n);

    }

    private void Count_Number_Of_Islands(int [][] matrix){
        int count=0;

        boolean [][]visited=new boolean[matrix.length][matrix[0].length];


        for(int i=0;i<matrix.length;i++){
            for(int j=0;j<matrix[i].length;j++){
                if(!visited[i][j] && matrix[i][j]!=0){  //If Current Block Is Not Visited
                    DFS(visited,matrix,i,j, matrix.length);
                    ++count;
                }
            }
        }
        System.out.println("The Total Number Of Islands Are: "+count);
    }

    public static void main(String []args){
        Graph_Number_Of_Islands gnp=new Graph_Number_Of_Islands();
        int [][]matrix={{1,1,0,0,0},
                        {0,1,0,0,1},
                        {1,0,0,1,1},
                        {0,0,0,0,0},
                        {1,0,1,1,0},
                        {0,0,0,0,0},
                        {1,0,1,0,1}};

        gnp.Count_Number_Of_Islands(matrix);
    }

}


