/*
 * @Description: 
 * @Version: 1.0
 * @Autor: like
 * @Date: 2022-06-08 11:08:17
 * @LastEditors: like
 * @LastEditTime: 2022-06-08 11:15:59
 */
#ifndef CV_COMMON_HPP
#define CV_COMMON_HPP
#include <opencv2/opencv.hpp>  
#include <opencv2/core/core.hpp>  
#include <opencv2/highgui/highgui.hpp>  
#include <opencv2/imgproc.hpp>  
#include <iostream>  
#include <vector>
using namespace std;  
using namespace cv;  

/**
 * @brief display cv image
 * 
 */
#define CV_DEBUG
#ifdef CV_DEBUG
#   define DISPLAY_IMAGE(img)do{imshow("image : " ##img, img);  }while(0)
#else
#   define DISPLAY_IMAGE(img)
#endif

//void Decompose3(const Mat& img, std::vector<cv::Mat>& channels)
//{
//	cv::split(img, channels);
//}
#define RGB2GRAY(img) cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#define DECOMPOSE3(img) do{  }while(0)
#endif