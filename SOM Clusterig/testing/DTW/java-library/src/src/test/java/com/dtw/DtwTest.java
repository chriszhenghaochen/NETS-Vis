package src.test.java.com.dtw;

/*
 * DtwTest.java   Jul 14, 2004
 *
 * Copyright (c) 2004 Stan Salvador
 * stansalvador@hotmail.com
 */

import java.io.FileNotFoundException;
import java.io.PrintWriter;

import src.main.java.com.timeseries.TimeSeries;
import src.main.java.com.util.DistanceFunction;
import src.main.java.com.util.DistanceFunctionFactory;
import src.main.java.com.dtw.TimeWarpInfo;

public class DtwTest {

	// PUBLIC FUNCTIONS
	public static void main(String[] args) throws FileNotFoundException {
		if (args.length != 2 && args.length != 3) {
			System.out
					.println("USAGE:  java DtwTest timeSeries1 timeSeries2 [EuclideanDistance|ManhattanDistance|BinaryDistance]");
			System.exit(1);
		} else {
			final TimeSeries tsI = new TimeSeries(args[0], false, false, ',');
			final TimeSeries tsJ = new TimeSeries(args[1], false, false, ',');

			final DistanceFunction distFn;
			if (args.length < 3) {
				distFn = DistanceFunctionFactory
						.getDistFnByName("EuclideanDistance");
			} else {
				distFn = DistanceFunctionFactory.getDistFnByName(args[2]);
			} // end if

			final TimeWarpInfo info = src.main.java.com.dtw.DTW
					.getWarpInfoBetween(tsI, tsJ, distFn);

			System.out.println("Warp Distance: " + info.getDistance());
			System.out.println("Warp Path:     " + info.getPath());
				
			
			
			//--------------write in file---------------------//
			String output = (String) info.getPath().toString();
			output = output.substring(1, output.length() - 2);
			output = output.replace("(", "");
			output = output.replace("),", "\n");
			//System.out.println(output);
			
			PrintWriter out = new PrintWriter("C:\\Users\\zchen4\\Desktop\\data\\output.txt");
			out.println(output);
			out.close();

		} // end if

	} // end main()

} // end class DtwTest
