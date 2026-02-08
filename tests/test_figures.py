import pdf_pipeline.figures as figures


def test_embedded_page_figure_limit_without_caption() -> None:
    assert figures._embedded_page_figure_limit(caption_count=0, dense_embedded_page=False) == 4
    assert figures._embedded_page_figure_limit(caption_count=0, dense_embedded_page=True) == 2


def test_embedded_page_figure_limit_with_caption() -> None:
    assert figures._embedded_page_figure_limit(caption_count=1, dense_embedded_page=False) == 1
    assert figures._embedded_page_figure_limit(caption_count=2, dense_embedded_page=False) == 2
    assert figures._embedded_page_figure_limit(caption_count=5, dense_embedded_page=False) == 2


def test_embedded_page_figure_limit_with_caption_and_dense_page() -> None:
    assert figures._embedded_page_figure_limit(caption_count=1, dense_embedded_page=True) == 1
    assert figures._embedded_page_figure_limit(caption_count=3, dense_embedded_page=True) == 1


def test_image_matches_any_caption_true_for_nearby_caption() -> None:
    image_bbox = (100.0, 100.0, 300.0, 220.0)
    caption_blocks = [("Figure 1", (110.0, 230.0, 290.0, 260.0))]
    assert figures._image_matches_any_caption(image_bbox, caption_blocks, page_height=800.0) is True


def test_image_matches_any_caption_false_for_far_caption() -> None:
    image_bbox = (100.0, 100.0, 300.0, 220.0)
    caption_blocks = [("Figure 1", (350.0, 600.0, 500.0, 630.0))]
    assert figures._image_matches_any_caption(image_bbox, caption_blocks, page_height=800.0) is False
